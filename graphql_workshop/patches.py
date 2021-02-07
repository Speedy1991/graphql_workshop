from asgiref.sync import sync_to_async
from graphene.types.schema import normalize_execute_kwargs
from graphql import ExecutionResult, GraphQLError, GraphQLSchema, create_source_event_stream, parse, validate
from graphql.execution.execute import (execute)
from graphql.language import DocumentNode
from graphql.subscription.map_async_iterator import MapAsyncIterator
from graphql.type import GraphQLFieldResolver
from inspect import isawaitable
from typing import (
    Any,
    AsyncIterator,
    Dict,
    Optional,
    Union,
)


async def _subscribe_graphql_patched(
        schema: GraphQLSchema,
        document: DocumentNode,
        root_value: Any = None,
        context_value: Any = None,
        variable_values: Optional[Dict[str, Any]] = None,
        operation_name: Optional[str] = None,
        field_resolver: Optional[GraphQLFieldResolver] = None,
        subscribe_field_resolver: Optional[GraphQLFieldResolver] = None,
) -> Union[AsyncIterator[ExecutionResult], ExecutionResult]:
    try:
        result_or_stream = await create_source_event_stream(
            schema,
            document,
            root_value,
            context_value,
            variable_values,
            operation_name,
            subscribe_field_resolver,
        )
    except GraphQLError as error:
        return ExecutionResult(data=None, errors=[error])
    if isinstance(result_or_stream, ExecutionResult):
        return result_or_stream

    async def map_source_to_response(payload: Any):
        if payload is None:
            return None
        result = sync_to_async(execute, thread_sensitive=True)(
            schema,
            document,
            payload,
            context_value,
            variable_values,
            operation_name,
            field_resolver
        )
        return await result if isawaitable(result) else result

    return MapAsyncIterator(result_or_stream, map_source_to_response)


async def subscribe_graphene_patched(self, query, *args, **kwargs):
    try:
        document = parse(query)
    except GraphQLError as error:
        return ExecutionResult(data=None, errors=[error])
    validation_errors = validate(self.graphql_schema, document)
    if validation_errors:
        return ExecutionResult(data=None, errors=validation_errors)
    kwargs = normalize_execute_kwargs(kwargs)
    return await _subscribe_graphql_patched(self.graphql_schema, document, *args, **kwargs)