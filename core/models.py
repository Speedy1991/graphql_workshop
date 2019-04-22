from django.db import models
from enum import IntEnum


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
