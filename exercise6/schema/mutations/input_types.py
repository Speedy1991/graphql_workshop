import graphene
from core.models import Semester
from ..types import SemesterTypeEnum


# QUESTION: Why should you use input types?
class StudentInputType(graphene.InputField):
    # TODO 4: Move the fields from AddStudentMutation.Arguments into this InputType
    # TODO 6: Refactor the semster field to use the SemesterTypeEnum
    pass
