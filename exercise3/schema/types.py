import graphene
from core import models
from graphene_django import DjangoObjectType


# TODO 1: Our custom Types need to inherit from DjangoObjectType
class ProfessorType(graphene.ObjectType):
    # TODO 2: Remove the fields, graphene_django will handle the custom fields for us
    id = graphene.ID()
    name = graphene.String(required=True)
    age = graphene.Int(required=True)

    # TODO 3: Implement the Meta information
    # DOCS: https://docs.graphene-python.org/projects/django/en/latest/queries/#only-fields
    #class Meta:
    #    model = models.Professor
    # INFO: Explicit is better than Implicit. graphene_django will expose ALL of the fields - even related ones
    #    only_fields = ("id", "name", "age")
    # INFO: Don't worry about the `modules` field - we will bring it back in the next exercise


class StudentType(DjangoObjectType):
    # TODO 4: Implement the Meta information
    pass


class ModuleType(DjangoObjectType):
    # TODO 5: Implement the Meta information
    pass
