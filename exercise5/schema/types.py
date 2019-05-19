import graphene
from core import models
from graphene_django import DjangoObjectType


class ProfessorType(DjangoObjectType):
    class Meta:
        model = models.Professor
        only_fields = ("id", "name", "age")


class StudentType(graphene.ObjectType):
    modules = graphene.List(lambda: ModuleType)

    class Meta:
        model = models.Student
        only_fields = ("id", "name", "age", "semester", "favourite_module")

    def resolve_modules(self, info, **kwargs):
        return self.module_set.all()


class ModuleType(graphene.ObjectType):
    class Meta:
        model = models.Module
        only_fields = ("id", "name", "professor", "students")
