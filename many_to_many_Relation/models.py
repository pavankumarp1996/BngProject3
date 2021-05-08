
from django.db import models

class Student(models.Model):
    Sno = models.IntegerField()
    Sname = models.CharField(max_length=10)
    Slocation = models.CharField(max_length=10)

class Course(models.Model):
    Student = models.ManyToManyField(Student)
    Cid = models.IntegerField()
    Cname = models.CharField(max_length=20)
    Cfee = models.IntegerField()
