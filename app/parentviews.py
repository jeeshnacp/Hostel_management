from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.models import Hostel, Food, Attendance, Fees, Student


@login_required(login_url='login')
def parent_dashboard(request):
    return render(request,'parent_temp/parent_dashboard.html')


@login_required(login_url='login')
def view_hostel(request):
    data=Hostel.objects.all()
    return render(request,'parent_temp/parent_view_hostel.html',{'data':data})

@login_required(login_url='login')
def view_food(request):
    data=Food.objects.all()
    return render(request,'parent_temp/parent_view_food.html',{'data':data})


@login_required(login_url='login')
def view_attendance(request):
    attendances=Attendance.objects.all()
    return render(request,'parent_temp/view_attendance.html',{'attendances':attendances})

@login_required(login_url='login')
def delete_account(request):
    user=request.user
    if request.method=='POST':
        user.delete()
        messages.info(request,'your account deleted successfull')
        return redirect('login')
    return render(request,'parent_temp/delete_profile.html')


def view_payments(request):
    payments = Fees.objects.all()
    return render(request,'parent_temp/view_payments.html',{'payments':payments})




