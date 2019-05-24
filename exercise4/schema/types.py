import graphene
from core import models
from graphene_django import DjangoObjectType


class ProfessorType(DjangoObjectType):

    class Meta:
        model = models.Professor
        only_fields = ("id", "name", "age")


class StudentType(DjangoObjectType):
    # TODO 1: Define a custom field "modules", resolving to a list of ModuleType's
    # HINT: Forward declaration

    class Meta:
        model = models.Student
        only_fields = ("id", "name", "age", "semester", "favourite_module")
    # TODO 0: We want all "modules" of a student. At the moment we only get the favourite_module. Continue with TODO 1
    # INFO: One way to archive this is to add "module_set" to "only_fields" but this will expose a endpoint called "moduleSet"

    # TODO 2: Write a custom resolver for the field `modules`
    # DJANGO: self.module_set.all() will return a list of connected Modules
    def resolve_modules(self, info, **kwargs):
        pass


class ModuleType(DjangoObjectType):

    class Meta:
        model = models.Module
        only_fields = ("id", "name", "professor", "students")
