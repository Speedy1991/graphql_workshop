import graphene
from ..types import StudentType
from core import models
from .input_types import StudentInputType


# QUESTION: How do you think, will a update Mutation look like?
class AddStudentMutation(graphene.Mutation):
    student = graphene.Field(StudentType)

    class Arguments:
        # TODO 0: Throw away this fields and add a student field (StudentInputType)
        # DOCS: https://docs.graphene-python.org/en/latest/types/mutations/#inputfields-and-inputobjecttypes
        name = graphene.String()
        age = graphene.Int()
        semester = graphene.Int()
        favourite_subject = graphene.ID(required=False)

    # TODO: 1: Refactor the mutate method. It will only receive self, info, student
    def mutate(self, info, name, age, semester):
        # TODO 2: Refactor the create method
        # DJANGO: We can do some kwargs spreading: models.Student.objects.create(**student)
        student = models.Student.objects.create(name=name, age=age, semester=semester)
        return AddStudentMutation(student=student)

# TODO 3: More Refactors in the input_types.py file and types.py

# EXTRA: Write a update Mutation to update the favourite_subject of a specific student. Don't forget to add it to the exercise6/schema/mutatoins/__init__.py file
