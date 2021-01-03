from enum import IntEnum
from django.db import models
from polymorphic.models import PolymorphicModel


class Semester(IntEnum):
    FIRST = 1
    SECOND = 2
    THIRD = 3

    def __str__(self):
        return str(self.value)


class Person(models.Model):
    name = models.CharField(max_length=32, unique=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Professor(Person):
    pass


class Student(Person):
    semester = models.IntegerField(choices=[(semester.value, semester) for semester in Semester])
    favourite_module = models.ForeignKey("core.Module", on_delete=models.SET_NULL, null=True, default=None, blank=True)


class Module(models.Model):
    name = models.CharField(max_length=32, unique=True)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return self.name


# Polymorphic Example
class Project(PolymorphicModel):
    topic = models.CharField(max_length=30)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True)


class ArtProject(Project):
    artist = models.CharField(max_length=30)


class ResearchProject(Project):
    supervisor = models.CharField(max_length=30)
