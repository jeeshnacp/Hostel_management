from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Login(AbstractUser):
    is_parent = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


class Hostel(models.Model):
    total_rooms = models.CharField(max_length=100)
    occupied = models.CharField(max_length=100)
    annual_expenses = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_no = models.IntegerField()
    room_facilities = models.TextField()


class Food(models.Model):
    breakfast = models.CharField(max_length=50)
    lunch = models.CharField(max_length=50)
    dinner = models.CharField(max_length=50)


class Complaint(models.Model):
    student=models.ForeignKey(Login,on_delete=models.DO_NOTHING,null=True)
    subject = models.CharField(max_length=50)
    date = models.DateField()
    complaint = models.TextField()
    reply=models.TextField(null=True,blank=True)


class Student(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True, related_name='student')
    name = models.CharField(max_length=50)
    address = models.TextField()
    contact_no = models.IntegerField()
    email = models.EmailField()
    approval_status = models.BooleanField(default=0)
    image = models.ImageField(upload_to='profile', null=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Parent(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, primary_key=True, related_name='parent')
    role = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    address = models.TextField()
    child_name = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    email = models.EmailField()
    approval_status = models.BooleanField(default=0)
    seen = models.BooleanField(default=False)


class Staff(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    address = models.TextField()
    contact_no = models.IntegerField()
    email = models.EmailField()


class Fees(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    room_rent = models.FloatField(default=0)
    mess_bill = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    status = models.BooleanField(default=False)
    paid_by = models.CharField(max_length=100)
    payment_date = models.DateField(null=True)
    payment = models.CharField(max_length=100)

    def get_total(self):
        return self.room_rent + self.mess_bill


class Payment(models.Model):
    bill = models.ForeignKey(Fees, on_delete=models.CASCADE, related_name='fee_payment')
    payment = models.CharField(max_length=100)
    card_no = models.CharField(max_length=100)
    card_cvv = models.CharField(max_length=100)
    expiry_month = models.CharField(max_length=100)
    expiry_year = models.CharField(max_length=100)


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance')
    date = models.DateField()
    attendance = models.CharField(max_length=100)
    time = models.TimeField()


class Notification(models.Model):
    notification = models.TextField(max_length=100)
    date = models.DateField()

class BookRoom(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    date_joining=models.DateField()
    booking_date=models.DateField(auto_now_add=True)
    status=models.IntegerField(default=0)
    booked_by=models.ForeignKey(Login,on_delete=models.CASCADE)
    seen=models.BooleanField(default=False)