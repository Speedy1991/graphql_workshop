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
    projects = graphene.List(lambda: ProjectInterface)

    class Meta:
        model = models.Professor
        only_fields = ("id", "name", "age")
        interfaces = (PersonInterface, )

    def resolve_modules(self, info, **kwargs):
        return self.module_set.all()

    def resolve_projects(self, info):
        return models.Project.objects.filter(professor=self)


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


class ProjectInterface(graphene.Interface):
    topic = graphene.String()
    students = graphene.List(StudentType)

    def resolve_students(self, info):
        return self.students.all()

    @classmethod
    def resolve_type(cls, instance, info):
        if isinstance(instance, models.ArtProject):
            return ArtProjectType
        elif isinstance(instance, models.ResearchProject):
            return ResearchProjectType
        raise Exception(f"Unexpected type: {instance}")


class ArtProjectType(DjangoObjectType):
    class Meta:
        model = models.ArtProject
        only_fields = ("id", "artist")
        interfaces = (ProjectInterface, )


class ResearchProjectType(DjangoObjectType):
    class Meta:
        model = models.ResearchProject
        only_fields = ("id", "supervisor")
        interfaces = (ProjectInterface, )
