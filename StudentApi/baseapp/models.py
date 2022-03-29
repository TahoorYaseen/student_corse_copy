from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    branch = models.CharField(max_length=50)
    cgpa = models.FloatField(null=True)
    username = None



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Courses(models.Model):
    student = models.ForeignKey(User,on_delete=models.CASCADE)
    courseName = models.CharField(max_length=200)
    courseFee = models.FloatField(null=True)
    courseTeacher = models.CharField(max_length=200)
    