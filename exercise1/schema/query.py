import graphene
from .types import ProfessorType, StudentType, ModuleType
from core.models import Student, Professor, Module


class Query(graphene.ObjectType):
    professors = graphene.List(ProfessorType)
    # TODO: students
    # TODO: modules

    def resolve_professors(self, info, **kwargs):
        return Professor.objects.all()  # HINT: See the README Django Cheatsheet

    # TODO: Write a resolver for students
    # TODO: Write a resolver for modules
