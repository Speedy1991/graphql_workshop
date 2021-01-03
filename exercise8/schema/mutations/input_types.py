import graphene
from ..types import SemesterTypeEnum


class StudentInputType(graphene.InputObjectType):
    name = graphene.String()
    age = graphene.Int()
    semester = SemesterTypeEnum()
    favourite_module = graphene.ID(required=False)
