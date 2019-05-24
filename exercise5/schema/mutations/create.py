import graphene
from ..types import StudentType
from core import models


# HINT: Hey Django Experts - did you know you can use DjangoFormMutations and DjangoModelFormMutations? That's a new awesome feature
# DOCS: Check it out https://docs.graphene-python.org/projects/django/en/latest/mutations/#djangomodelformmutation
# I won't explain it in the workshop because this is only Django related - but feel free to talk about this feature with me in the breaks :)
class AddStudentMutation(graphene.Mutation):
    # DOCS: https://docs.graphene-python.org/projects/django/en/latest/mutations/#simple-example
    # TODO 0: The mutation has a student field (StudentType)
    student = graphene.Field(StudentType)

    class Arguments:
        # TODO 1: Define the fields, needed to create a student (name, age, semester)
        # HINT: semester is an integer
        pass

    # HINT: Every mutation needs a mutate method. The mutate method is called with self, info, **arguments
    def mutate(self, info, name, age, semester):
        # TODO 2: Create a new Student
        # DJANGO: models.Student.objects.create(name=name, age=age, semester=semester)
        # TODO 3: Return a Instance of AddStudentMutation with the new student as kwarg
        pass
