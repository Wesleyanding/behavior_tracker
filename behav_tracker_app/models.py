from django.db import models
from django.contrib.auth.models import AbstractUser

class Behavior(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    antecedent = models.CharField(max_length=50)
    behavior = models.CharField(max_length=50)
    intervention = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.behavior

class Class(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=20)
    grade = models.CharField(max_length=3)
    behavior = models.ManyToManyField(Behavior, related_name='students', blank=True,)
    classes = models.ManyToManyField(Class, related_name='students', blank=True)

    def __str__ (self):
        return self.name

class Teacher(AbstractUser):
    name = models.CharField(max_length=20)
    classes = models.ManyToManyField(Class, related_name='teacher', blank=True)
    student = models.ManyToManyField(Student, related_name='teacher', blank=True)
    admin = models.BooleanField(default=False)



    
