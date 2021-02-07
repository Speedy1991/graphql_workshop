import graphene
from ..types import StudentType
from core import models
from .input_types import StudentInputType


class AddStudentMutation(graphene.Mutation):
    student = graphene.Field(StudentType)

    class Arguments:
        student_input = StudentInputType(required=True)

    def mutate(self, info, student_input):
        student = models.Student.objects.create(**student_input)
        return AddStudentMutation(student=student)
