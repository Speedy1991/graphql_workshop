import graphene
from .create import AddStudentMutation


class Mutation(graphene.ObjectType):
    add_student = AddStudentMutation.Field()
