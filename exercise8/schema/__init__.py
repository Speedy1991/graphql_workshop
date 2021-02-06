import graphene
from .query import Query
from .mutations import Mutation
# TODO 7 We need to import ResearchProjectType and ArtProjectType

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    # TODO 8 ResearchProjectType, ArtProjectType are never referenced directly, therefore we must tell graphql about them
    # types=[ResearchProjectType, ArtProjectType]
)
