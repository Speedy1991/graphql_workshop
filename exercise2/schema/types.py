import graphene


class ProfessorType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    age = graphene.Int(required=True)
    # TODO: add a List of ModuleType's
    # DOCS: https://docs.graphene-python.org/en/latest/types/list-and-nonnull/
    # HINT: We need a forward declaration because the ModuleType isn't defined at this place graphene.List(lambda: ModuleType)

    def resolve_modules(self, info, **kwargs):
        pass
        # TODO: Resolve the modules
        # HINT: self is the current instance (in this case a professor instance)
        # DJANGO: instance.modules_set.all()


class StudentType(graphene.ObjectType):
    id = graphene.ID()
    age = graphene.Int(required=True)
    name = graphene.String(required=True)
    semester = graphene.Int(required=True)

    # TODO: Resolve the modules
    # HINT: self is the current instance (in this case a student instance)
    # DJANGO: instance.modules_set.all()


class ModuleType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    # TODO: Add a ProfessorType field

    def resolve_professor(self, info, **kwargs):
        pass
        # TODO: resolve the professor of the module
        # HINT: self is the current instance (in this case a module instance)
