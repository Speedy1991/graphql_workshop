import graphene
from .types import ProfessorType, StudentType, ModuleType
from core.models import Student, Professor, Module

# QUESTION: Why can't we use a DjangoObjectType on the main Query?
class Query(graphene.ObjectType):
    professors = graphene.List(ProfessorType)
    students = graphene.List(StudentType)
    modules = graphene.List(ModuleType)

    def resolve_professors(self, info, **kwargs):
        return Professor.objects.all()

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_modules(self, info, **kwargs):
        return Module.objects.all()
