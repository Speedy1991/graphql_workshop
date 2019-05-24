import graphene
from ..types import SemesterTypeEnum


# QUESTION: Why should you use input types?
class StudentInputType(graphene.InputObjectType):
    # TODO 4: Move the fields from AddStudentMutation.Arguments into this InputType
    # TODO 6: Refactor the semester field to use the SemesterTypeEnum
    pass
