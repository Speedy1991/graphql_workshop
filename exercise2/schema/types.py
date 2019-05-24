import graphene


class ProfessorType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    age = graphene.Int(required=True)
    # TODO 1: add a List of modules
    # DOCS: https://docs.graphene-python.org/en/latest/types/list-and-nonnull/
    # HINT: We need a forward declaration because the ModuleType isn't defined at this place graphene.List(lambda: ModuleType)

    def resolve_modules(self, info, **kwargs):
        pass
        # TODO 2: Resolve the modules
        # HINT: self is the current instance (in this case a professor instance)
        # DJANGO: instance.module_set.all()


class StudentType(graphene.ObjectType):
    id = graphene.ID()
    age = graphene.Int(required=True)
    name = graphene.String(required=True)
    semester = graphene.String(required=True)
    # TODO 3: add modules
    # TODO 4: add favourite_subject

    # TODO 5: Resolve the modules
    # HINT: self is the current instance (in this case a student instance)
    # DJANGO: instance.module_set.all()
    # TODO 6: Resolve favourite_module


class ModuleType(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String(required=True)
    # TODO 7: Add professor

    def resolve_professor(self, info, **kwargs):
        pass
        # TODO 8: resolve the professor
        # HINT: self is the current instance (in this case a module instance)
