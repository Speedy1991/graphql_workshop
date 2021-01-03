import graphene
from core import models
from graphene_django import DjangoObjectType


class PersonInterface(graphene.Interface):
    # TODO 1: add fields to resolve common fields: id, name, age

    @classmethod
    def resolve_type(cls, instance, info):
        pass
        # TODO 2: check if instance isinstance of Professor or Student and return the type
        # TODO 3: throw an exception if no type matches


class ProfessorType(DjangoObjectType):
    modules = graphene.List(lambda: ModuleType)

    class Meta:
        model = models.Professor
        only_fields = ()
        # TODO 4: Add the interface
        # interfaces = (PersonInterface, )

    def resolve_modules(self, info, **kwargs):
        return self.module_set.all()


class StudentType(DjangoObjectType):
    modules = graphene.List(lambda: ModuleType)

    class Meta:
        model = models.Student
        only_fields = ("semester", "favourite_module")
        # TODO 5: Add the interface

    def resolve_modules(self, info, **kwargs):
        return self.module_set.all()


class ModuleType(DjangoObjectType):

    class Meta:
        model = models.Module
        only_fields = ("id", "name", "professor", "students")


SemesterTypeEnum = graphene.Enum.from_enum(models.Semester)
