import graphene
from .create import AddStudentMutation
from .update import UpdateStudentMutation


class Mutation(graphene.ObjectType):
    add_student = AddStudentMutation.Field()
    update_student = UpdateStudentMutation.Field()
