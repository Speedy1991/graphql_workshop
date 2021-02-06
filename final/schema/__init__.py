import graphene
from .query import Query
from .mutations import Mutation
from .types import ResearchProjectType, ArtProjectType

schema = graphene.Schema(query=Query, mutation=Mutation, types=[ResearchProjectType, ArtProjectType])
