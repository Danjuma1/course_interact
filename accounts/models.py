from django.db import models
from django.contrib.auth.models import User


class Lecturer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    matric_no = models.CharField(max_length=10)
    course_list = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
