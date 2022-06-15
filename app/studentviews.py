from django.contrib import messages
from django.shortcuts import render, redirect

from app.form import complaintsform, studentregister, StudentBookRoomForm
from app.models import Hostel, Food, Attendance, Student, BookRoom


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
    return render(request, 'student_temp/Register_complaint.html', {'form': form})


def view_attendance(request):
    u = Student.objects.get(user=request.user)
    attendance = Attendance.objects.filter(student=u)
    context = {
        'attendance': attendance
    }
    return render(request, 'student_temp/view_attendances.html', context)


def view_profile(request):
    profile = Student.objects.filter(user=request.user)
    return render(request, 'student_temp/view_profile.html', {'profile': profile})


def update_profile(request):
    n = Student.objects.get(user=request.user)
    form=studentregister(instance=n)
    if request.method == 'POST':
        form = studentregister(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request,'profile updated successfull')
            return redirect('profile')
    return render(request, 'student_temp/update_profile.html', {'form': form})


def book_room(request):
    form=StudentBookRoomForm()
    if request.method=='POST':
        form=StudentBookRoomForm(request.POST)
        if form.is_valid():
            book=form.save(commit=False)
            book.student=Student.objects.get(user=request.user)
            book.date_joining=form.cleaned_data.get('date_joining')
            book.booking_date=form.cleaned_data.get('booking_date')
            book.booked_by=request.user
            student_qs=BookRoom.objects.filter(student=Student.objects.get(user=request.user))
            if student_qs.exists():
                messages.info(request,'you have already booked room')
            else:
                book.save()
                messages.info(request,'successfully booked room')
                return redirect('booking_status')
    return render(request,'student_temp/booking_room.html',{'form':form})


def booking_status(request):
    student=Student.objects.get(user=request.user)
    status=BookRoom.objects.filter(student=student)
    return render(request,'student_temp/booking_status.html',{'status':status})

def delete_student_profile(request):
    user=request.user
    if request.method=='POST':
        user.delete()
        messages.info(request,'your account deleted successfull')
        return redirect('login')
    return render(request,'student_temp/delete_profile.html')


def delete_profile(request):
    user=request.user
    if request.method=='POST':
        user.delete()
        messages.info(request,'your account deleted successfull')
        return redirect('login')
    return render(request,'student_temp/delete_profile.html')
