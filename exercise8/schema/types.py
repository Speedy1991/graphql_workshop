import graphene
from core import models
from graphene_django import DjangoObjectType

SemesterTypeEnum = graphene.Enum.from_enum(models.Semester)


class PersonInterface(graphene.Interface):
    id = graphene.ID(required=True)
    name = graphene.String(required=True)
    age = graphene.String(required=True)

    @classmethod
    def resolve_type(cls, instance, info):
        if isinstance(instance, models.Professor):
            return ProfessorType
        if isinstance(instance, models.Student):
            return StudentType
        raise Exception(f"Unexpected type: {instance}")


class ProfessorType(DjangoObjectType):
    modules = graphene.List(lambda: ModuleType)

    class Meta:
        model = models.Professor
        only_fields = ("id", "name", "age")
        interfaces = (PersonInterface, )

    def resolve_modules(self, info, **kwargs):
        return self.module_set.all()


class StudentType(DjangoObjectType):
    modules = graphene.List(lambda: ModuleType)
    semester = SemesterTypeEnum()

    class Meta:
        model = models.Student
        only_fields = ("id", "name", "age", "favourite_module")
        interfaces = (PersonInterface,)

    def resolve_modules(self, info, **kwargs):
        return self.module_set.all()


class ModuleType(DjangoObjectType):

    class Meta:
        model = models.Module
        only_fields = ("id", "name", "professor", "students")
