from django.contrib import admin
from polymorphic.admin import PolymorphicInlineSupportMixin, StackedPolymorphicInline
from . import models


class ProjectInline(StackedPolymorphicInline):
    class ArtProjectInline(StackedPolymorphicInline.Child):
        model = models.ArtProject

    class ResearchProjectInline(StackedPolymorphicInline.Child):
        model = models.ResearchProject

    model = models.Project
    child_inlines = (
        ArtProjectInline,
        ResearchProjectInline
    )


@admin.register(models.Module)
class ModuleAdmin(admin.ModelAdmin):
    filter_horizontal = ["students"]
    autocomplete_fields = ["professor"]
    search_fields = ["name"]


@admin.register(models.Professor)
class ProfessorAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    search_fields = ["name"]
    inlines = [ProjectInline]


@admin.register(models.Student)
class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ["favourite_module"]
    list_display = ["name", "favourite_module"]

