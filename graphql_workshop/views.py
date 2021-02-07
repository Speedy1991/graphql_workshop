import asyncio
import types

from django.conf import settings
import websockets
from asgiref.sync import sync_to_async
from django.contrib.sessions.models import Session
from django.core.handlers.asgi import ASGIRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseForbidden
from django.middleware.csrf import _compare_masked_tokens, _sanitize_token
from starlette.websockets import WebSocketDisconnect
from django.contrib.auth import get_user_model

from final.schema import schema as final_schema
from .patches import subscribe_graphene_patched

UserModel = get_user_model()


def _get_user(socket, message):
    csrf_from_message = message.get('payload', dict()).get('csrfToken', None)
    host = socket.headers.get('host', None)
    session_id = socket.cookies.get('sessionid', None)
    csrf_from_cookies = socket.cookies.get('csrftoken', None)

    if session_id and host and csrf_from_cookies and csrf_from_message and _compare_masked_tokens(
            _sanitize_token(csrf_from_message), _sanitize_token(csrf_from_cookies)):
        pass
    else:
        return

    session = Session.objects.filter(session_key=session_id).first()
    if not session:
        return
    session_data = session.get_decoded()
    uid = session_data.get('_auth_user_id', None)
    if not uid:
        return
    user = UserModel.objects.filter(id=uid).first()
    if not user or user.id is None:
        return
    return user


def _recheck_user(cookies, user_id):
    session_id = cookies.get('sessionid', None)
    session = Session.objects.filter(session_key=session_id).first()
    if not session:
        return False
    session_data = session.get_decoded()
    uid = session_data.get('_auth_user_id', None)
    if not uid:
        return False
    return uid == str(user_id)


class AttrDict:
    def __init__(self, data):
        self.data = data or {}

    def __getattr__(self, item):
        return self.get(item)

    def get(self, item):
        return self.data.get(item)


async def _result_handler(_req_id, _result, socket, user_id):
    try:
        async for item in _result:
            if item is None:
                return
            if not await sync_to_async(_recheck_user, thread_sensitive=True)(socket.cookies, user_id):
                raise Exception("Invalid user state")
            errors = _result.errors
            if errors:
                await socket.send_json({
                    "id": _req_id,
                    "type": "error",
                    "payload": list(map(str, errors)),
                })
            else:
                await socket.send_json({
                    "id": _req_id,
                    "type": "next",
                    "payload": {
                        "data": _result.data,
                    },
                })
    finally:
        await _result.aclose()


async def graphql_websocket_view(socket):
    if isinstance(socket, WSGIRequest) or isinstance(socket, ASGIRequest):
        return HttpResponseForbidden()

    subscriptions = dict()
    try:
        await socket.accept(subprotocol='graphql-transport-ws')
        if not settings.GRAPHQL_SUBSCRIPTIONS_ENABLED:
            await socket.close(4499)
            raise WebSocketDisconnect
        user = None
        graphql_init = False
        while True:
            try:
                message = await socket.receive_json()
            except AssertionError:
                raise WebSocketDisconnect
            req_id = message.get('id', None)
            if message["type"] == "connection_init":
                if graphql_init:
                    await socket.close(4429)
                    break
                else:
                    graphql_init = True
                user = await sync_to_async(_get_user, thread_sensitive=True)(socket, message)
                if user:
                    await socket.send_json(dict(type="connection_ack"))
                else:
                    await socket.close(4401)
                    break
            elif message["type"] == "subscribe" and user and graphql_init and len(subscriptions) <= 20 and req_id:
                payload = message["payload"]
                subscription_key = f'{payload.get("operationName", None)}{payload.get("variables", None)}'
                for sub_item in subscriptions.values():
                    if sub_item.get('key') == subscription_key:
                        await socket.close(4409)
                        break
                if req_id in subscriptions:
                    await socket.close(4409)
                    break
                context = AttrDict(
                    dict(member=user, user=user, org=user.organization, ws_client=socket.scope.get('client', None)))

                schema = final_schema.schema_for_subscription
                setattr(schema, schema.subscribe.__name__, types.MethodType(subscribe_graphene_patched, schema))

                result = await schema.subscribe(
                    payload["query"],
                    operation_name=payload.get("operationName"),
                    variables=payload.get("variables"),
                    context=context,
                )

                task = asyncio.ensure_future(_result_handler(req_id, result, socket, user.id))
                subscriptions[req_id] = dict(task=task, req_id=req_id, key=subscription_key)
            elif message["type"] == "complete":
                sub = subscriptions.get(req_id, None)
                if sub:
                    task = sub.get('task', None)
                    if task and not task.cancelled():
                        task.cancel()
                subscriptions.pop(req_id, None)

            else:
                await socket.close(4403)
                break
    except (WebSocketDisconnect, websockets.exceptions.WebSocketException, RuntimeError):
        pass
    finally:
        for sub in subscriptions.values():
            task = sub.get('task', None)
            if task and not task.cancelled():
                task.cancel()
