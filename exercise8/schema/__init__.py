import graphene
from .query import Query
from .mutations import Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
