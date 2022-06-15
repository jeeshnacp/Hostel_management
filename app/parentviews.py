from django.contrib import messages
from django.shortcuts import render, redirect

from app.models import Hostel, Food, Staff, Attendance


def view_hostel(request):
    data=Hostel.objects.all()
    return render(request,'parent_temp/parent_view_hostel.html',{'data':data})

def view_food(request):
    data=Food.objects.all()
    return render(request,'parent_temp/parent_view_food.html',{'data':data})

def view_staff(request):
    data=Staff.objects.all()
    return render(request,'parent_temp/parent_view_staff.html',{'data':data})

def view_attendance(request):
    attendances=Attendance.objects.all()
    return render(request,'parent_temp/view_attendance.html',{'attendances':attendances})

def delete_account(request):
    user=request.user
    if request.method=='POST':
        user.delete()
        messages.info(request,'your account deleted successfull')
        return redirect('login')
    return render(request,'parent_temp/delete_profile.html')



