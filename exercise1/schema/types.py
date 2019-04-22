import graphene


class ProfessorType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    # TODO: Add a Scalar to resolve the age
    # https://docs.graphene-python.org/en/latest/types/scalars/


class StudentType(graphene.ObjectType):
    pass
    # TODO: id
    # TODO: age
    # TODO: name
    # TODO: semester


class ModuleType(graphene.ObjectType):
    pass
    # TODO: id
    # TODO: name
