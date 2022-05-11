from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_parent=models.BooleanField(default=False)
    is_student=models.BooleanField(default=False)\

class hostel(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    contact_no=models.IntegerField()
    email=models.EmailField()

class food(models.Model):
    breakfast=models.CharField(max_length=50)
    lunch=models.CharField(max_length=50)
    dinner=models.CharField(max_length=50)

class complaint(models.Model):
    subject=models.CharField(max_length=50)
    complaint=models.TextField()
    date=models.DateField()

