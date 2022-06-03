from django.contrib import messages
from django.shortcuts import render, redirect

from app.form import complaintsform
from app.models import hostel, food, attendance, student


def view_hostel(request):
    data = hostel.objects.all()
    return render(request, 'student_temp/student_view_hostel.html', {'data': data})


def view_food(request):
    data = food.objects.all()
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


def view_attend(request,id):
    u = student.objects.get(id=id)
    data = attendance.objects.filter(user=u)
    context = {
        'data': data
    }
    return render(request, 'student_temp/view_attendances.html', context)


