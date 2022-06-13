from django.contrib import messages
from django.shortcuts import render, redirect

from app.form import complaintsform, studentregister
from app.models import Hostel, Food, Attendance, Student


def view_hostel(request):
    data = Hostel.objects.all()
    return render(request, 'student_temp/student_view_hostel.html', {'data': data})


def view_food(request):
    data = Food.objects.all()
    return render(request, 'student_temp/student_view_food.html', {'data': data})


def register_complaint(request):
    if request.method == 'POST':
        form = complaintsform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfull')
            return redirect('student_home')
    else:
        form = complaintsform()
    return render(request, 'student_temp/Register_complaint.html', {'form':form})


def view_attendance(request):
    u = Student.objects.get(user=request.user)
    attendance = Attendance.objects.filter(student=u)
    context = {
        'attendance': attendance
    }
    return render(request, 'student_temp/view_attendances.html', context)

def view_profile(request):
    profile=Student.objects.filter(user=request.user)
    return render(request,'student_temp/view_profile.html',{'profile':profile})

def update_profile(request,id):
    n = Student.objects.get(id=id)
    if request.method == 'POST':
        form = studentregister(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = studentregister(request.POST or None, instance=n)
    return render(request, 'student_temp/update_profile.html', {'form': form})



