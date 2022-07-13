import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.form import complaintsform, studentregister, StudentBookRoomForm, PayBillForm
from app.models import Hostel, Food, Attendance, Student, BookRoom, Fees, Complaint


@login_required(login_url='login')
def student_dashboard(request):
    return render(request, 'student_temp/student_dashboard.html')


@login_required(login_url='login')
def view_hostel(request):
    data = Hostel.objects.all()
    return render(request, 'student_temp/student_view_hostel.html', {'data': data})


@login_required(login_url='login')
def view_food(request):
    data = Food.objects.all()
    return render(request, 'student_temp/student_view_food.html', {'data': data})


@login_required(login_url='login')
def register_complaint(request):
    form = complaintsform()
    u = request.user
    if request.method == 'POST':
        form = complaintsform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.student = u
            obj.save()
            messages.info(request, 'successfull')
            return redirect('view_complaint')
    else:
        form = complaintsform()
    return render(request, 'student_temp/Register_complaint.html', {'form': form})


@login_required(login_url='login')
def view_attendance(request):
    u = Student.objects.get(user=request.user)
    attendance = Attendance.objects.filter(student=u)
    context = {
        'attendance': attendance
    }
    return render(request, 'student_temp/view_attendances.html', context)


@login_required(login_url='login')
def view_profile(request):
    profile = Student.objects.filter(user=request.user)
    return render(request, 'student_temp/view_profile.html', {'profile': profile})


@login_required(login_url='login')
def update_profile(request):
    n = Student.objects.get(user=request.user)
    form = studentregister(instance=n)
    if request.method == 'POST':
        form = studentregister(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, 'profile updated successfull')
            return redirect('profile')
    return render(request, 'student_temp/update_profile.html', {'form': form})


@login_required(login_url='login')
def book_room(request):
    form = StudentBookRoomForm()
    if request.method == 'POST':
        form = StudentBookRoomForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.student = Student.objects.get(user=request.user)
            book.date_joining = form.cleaned_data.get('date_joining')
            book.booking_date = form.cleaned_data.get('booking_date')
            book.booked_by = request.user
            student_qs = BookRoom.objects.filter(student=Student.objects.get(user=request.user))
            if student_qs.exists():
                messages.info(request, 'you have already booked room')
            else:
                book.save()
                messages.info(request, 'successfully booked room')
                return redirect('booking_status')
    return render(request, 'student_temp/booking_room.html', {'form': form})


@login_required(login_url='login')
def booking_status(request):
    student = Student.objects.get(user=request.user)
    status = BookRoom.objects.filter(student=student)
    return render(request, 'student_temp/booking_status.html', {'status': status})


@login_required(login_url='login')
def cancel_booking(request, id):
    book = BookRoom.objects.filter(pk=id)
    if request.method == 'POST':
        book.delete()
        messages.info(request, 'your booking has been cancelled')
        return redirect('booking_status')
    return render(request, 'student_temp/cancel_booking.html')


@login_required(login_url='login')
def delete_profile(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        messages.info(request, 'your account deleted successfull')
        return redirect('login')
    return render(request, 'student_temp/delete_profile.html')


@login_required(login_url='login')
def payment_details(request):
    u = Student.objects.get(user=request.user)
    payment = Fees.objects.filter(student=u)
    return render(request, 'student_temp/payment_status.html', {'payment': payment})


@login_required(login_url='login')
def view_fee(request):
    u = Student.objects.get(user=request.user)
    fee = Fees.objects.filter(student=u, status=False)
    return render(request, 'student_temp/fees_view_student.html', {'fees': fee})


@login_required(login_url='login')
def view_complaint(request):
    data = Complaint.objects.filter(student=request.user)
    return render(request, 'student_temp/view_complaint.html', {'data': data})


@login_required(login_url='login')
def do_payment(request, id):
    u = Student.objects.get(user=request.user)
    fee = Fees.objects.get(id=id)
    amount = fee.get_total()
    form = PayBillForm(request.POST)
    if form.is_valid():
        p = form.save(commit=False)
        p.payment = amount
        p.bill = fee
        p.save()
        fee.status = True
        fee.paid_by = u.name
        fee.payment = amount
        fee.paid_date = datetime.date.today()
        fee.save()
        messages.info(request, 'fee paid successfully')
        return redirect('payment_details')
    return render(request, 'student_temp/do_payment.html', {'form': form})


def view_payment(request):
    data = Fees.objects.filter(student=request.user)
    return render(request, 'student_temp/payment_details.html', {'data': data})
