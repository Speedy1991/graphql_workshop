import graphene
from core import models
# TODO: Import DjangoObjectType from graphene_django
# from graphene_django import DjangoObjectType

# TODO: Our custom Types need to inherit from DjangoObjectType
class ProfessorType(graphene.ObjectType):
    # TODO: Remove the fields, graphene_django will handle the custom fields for us
    id = graphene.ID()
    name = graphene.String(required=True)
    age = graphene.Int(required=True)

    # TODO: Implement the Meta information
    # DOCS: https://docs.graphene-python.org/projects/django/en/latest/queries/#only-fields
    #class Meta:
    #    model = models.Professor
    # INFO: Explicit is better than Implicit. graphene_django will expose ALL of the fields - even related ones
    #    only_fields = ("id", "name", "age")

    # QUESTION: Why do you not need to resolve the professor field?
    #def resolve_modules(self, info, **kwargs):
    #    ...


class StudentType(graphene.ObjectType):
    # TODO: Implement the Meta information
    pass


class ModuleType(graphene.ObjectType):
    # TODO: Implement the Meta information
    pass
