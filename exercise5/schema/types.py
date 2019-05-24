import graphene
from core import models
from graphene_django import DjangoObjectType


class ProfessorType(DjangoObjectType):
    modules = graphene.List(lambda: ModuleType)

    class Meta:
        model = models.Professor
        only_fields = ("id", "name", "age")

    def resolve_modules(self, info, **kwargs):
        return self.module_set.all()


class StudentType(DjangoObjectType):
    modules = graphene.List(lambda: ModuleType)

    class Meta:
        model = models.Student
        only_fields = ("id", "name", "age", "semester", "favourite_module")

    def resolve_modules(self, info, **kwargs):
        return self.module_set.all()


class ModuleType(DjangoObjectType):

    class Meta:
        model = models.Module
        only_fields = ("id", "name", "professor", "students")
