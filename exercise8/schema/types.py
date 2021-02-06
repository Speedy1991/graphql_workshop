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
        # Hint 1
        if isinstance(instance, models.Professor):
            return ProfessorType
        if isinstance(instance, models.Student):
            return StudentType
        raise Exception(f"Unexpected type: {instance}")


class ProfessorType(DjangoObjectType):
    modules = graphene.List(lambda: ModuleType)
    # TODO 5 we need a forward declaration for the ProjectInterface

    class Meta:
        model = models.Professor
        only_fields = ("id", "name", "age")
        interfaces = (PersonInterface, )

    def resolve_modules(self, info, **kwargs):
        return self.module_set.all()

    def resolve_projects(self, info):
        # TODO 6 return a polymorphic queryset (returning ResearchProjects and ArtProjects)
        # DOCS https://django-polymorphic.readthedocs.io/en/stable/quickstart.html#using-polymorphic-models
        pass


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
    # TODO 4  topic and students are shared fields - add them to the interface

    def resolve_students(self, info):
        # Info: This is not a DjangoObjectType but an interface - therefore it is in our responsibility to resolve the students
        return self.students.all()

    @classmethod
    def resolve_type(cls, instance, info):
        # TODO 1: Write the type resolver (look at Hint1)
        raise Exception(f"Unexpected type: {instance}")


class ArtProjectType(DjangoObjectType):
    class Meta:
        model = models.ArtProject  # Info <-- this is a polymorphic model
        only_fields = ("id", "artist")
        # TODO 2 add the interface


class ResearchProjectType(DjangoObjectType):
    class Meta:
        model = models.ResearchProject  # Info <-- this is a polymorphic model
        only_fields = ("id", "supervisor")
        # TODO 3 add the interface
