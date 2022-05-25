from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_parent = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class hostel(models.Model):
    total_rooms = models.CharField(max_length=100)
    occupied = models.CharField(max_length=100)
    annual_expenses = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    room_facilities = models.TextField()


class food(models.Model):
    breakfast = models.CharField(max_length=50)
    lunch = models.CharField(max_length=50)
    dinner = models.CharField(max_length=50)


class complaint(models.Model):
    subject = models.CharField(max_length=50)
    date = models.DateField()
    complaint = models.TextField()


class student(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True, related_name='student')
    role = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    address = models.TextField()
    contact_no = models.IntegerField()
    email = models.EmailField()
    approval_status = models.BooleanField(default=0)
    image = models.ImageField(upload_to='profile', null=True)
    seen = models.BooleanField(default=False)


class parent(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True, related_name='parent')
    role = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    address = models.TextField()
    child_name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email = models.EmailField()
    approval_status = models.BooleanField(default=0)
    seen = models.BooleanField(default=False)


class staff(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    address = models.TextField()
    contact_no = models.IntegerField()
    email = models.EmailField()


class fees(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    room_rent = models.FloatField(default=0)
    mess_bill = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    paid_by = models.CharField(max_length=100)
    payment_date = models.DateField()
    payment = models.CharField(max_length=100)


class attendance(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    attendance = models.CharField(max_length=100)
    time = models.TimeField()
