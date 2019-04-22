from django.contrib import admin
from . import models


class ModuleAdmin(admin.ModelAdmin):
    filter_horizontal = ["students"]
    autocomplete_fields = ["professor"]
    search_fields = ["name"]


class ProfessorAdmin(admin.ModelAdmin):
    search_fields = ["name"]


class StudentAdmin(admin.ModelAdmin):
    autocomplete_fields = ["favourite_module"]


admin.site.register(models.Professor, ProfessorAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Module, ModuleAdmin)
