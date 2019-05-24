import graphene
from ..types import StudentType
from core import models
from .input_types import StudentInputType
from django.db import transaction


class UpdateStudentMutation(graphene.Mutation):
    student = graphene.Field(StudentType)

    class Arguments:
        pk = graphene.ID()
        student_input = StudentInputType(required=True)

    @transaction.atomic
    def mutate(self, info, student_input, pk):
        student = models.Student.objects.get(id=pk)
        for k, v in student_input.items():
            setattr(student, k, v)
        student.save()
        return UpdateStudentMutation(student=student)
