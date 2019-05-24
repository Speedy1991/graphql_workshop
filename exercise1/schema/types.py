import graphene


# DOCS: https://docs.graphene-python.org/en/latest/types/scalars/
class ProfessorType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    # TODO 1: add a field to resolve the age


class StudentType(graphene.ObjectType):
    pass
    # TODO 2: id
    # TODO 3: age
    # TODO 4: name
    # TODO 5: semester (String)


class ModuleType(graphene.ObjectType):
    pass
    # TODO 6: id
    # TODO 7: name
