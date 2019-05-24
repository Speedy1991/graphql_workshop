import graphene
from .types import ProfessorType, StudentType, ModuleType
from core.models import Student, Professor, Module


class Query(graphene.ObjectType):
    professors = graphene.List(ProfessorType)  # DOCS: https://docs.graphene-python.org/en/latest/types/list-and-nonnull/#list
    # TODO 8: students
    # TODO 9: modules

    def resolve_professors(self, info, **kwargs):
        return Professor.objects.all()  # DOCS: https://docs.djangoproject.com/en/2.2/topics/db/queries/#retrieving-all-objects

    # TODO 10: Write a resolver for students
    # TODO 11: Write a resolver for modules
