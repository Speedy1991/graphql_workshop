import graphene
from .types import ProfessorType, StudentType, ModuleType, PersonInterface
from core.models import Student, Professor, Module


class Query(graphene.ObjectType):
    professors = graphene.List(ProfessorType)
    students = graphene.List(StudentType)
    modules = graphene.List(ModuleType, starts_with=graphene.String(required=False))
    # TODO 6: add people which is a List of PersonInterface
    people = graphene.List(PersonInterface, required=True)

    def resolve_professors(self, info, **kwargs):
        return Professor.objects.all()

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_modules(self, info, starts_with=None, **kwargs):
        if starts_with is None:
            return Module.objects.all()
        return Module.objects.filter(name__startswith=starts_with)

    # TODO 7: Uncomment this resolver
    #def resolve_people(self, info):
    #    return [*Professor.objects.all(), *Student.objects.all()]
