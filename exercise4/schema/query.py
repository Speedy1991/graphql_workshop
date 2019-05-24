import graphene
from .types import ProfessorType, StudentType, ModuleType
from core.models import Student, Professor, Module


class Query(graphene.ObjectType):
    professors = graphene.List(ProfessorType)
    students = graphene.List(StudentType)

    # TODO 3: Add an optional argument to modules "starts_with". starts_with should be a StringType
    # DOCS: https://docs.graphene-python.org/projects/django/en/latest/queries/#full-example
    modules = graphene.List(ModuleType)

    def resolve_professors(self, info, **kwargs):
        return Professor.objects.all()

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

    # TODO 4: modules will receive an extra kwarg "starts_with", add it to the methods definition
    # HINT: Don't forget to set the default None if the argument is not provided
    def resolve_modules(self, info, starts_with=None, **kwargs):
        return Module.objects.all()
        # TODO 5: Fix the query, to return only modules starting with the given argument. Return all Modules if no filter argument is provided
        # DJANGO: Module.objects.filter(name__startswith=starts_with) will filter the results
