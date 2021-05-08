from django.db import models

class Student(models.Model):
    Sno = models.IntegerField()
    Sname = models.CharField(max_length=10)
    Slocation = models.CharField(max_length=10)
    def __str__(self):
       return self.Sname

class Course(models.Model):
    Student = models.OneToOneField(Student,on_delete=models.CASCADE)
    Cid = models.IntegerField()
    Cname = models.CharField(max_length=20)
    Cfee = models.IntegerField()
    def __str__(self):
        return self.Cname
