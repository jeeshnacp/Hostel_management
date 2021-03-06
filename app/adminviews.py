import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from app.form import hostelform, foods, staffform, feesform, notificationform, bill_form
from app.models import Hostel, Food, Complaint, Staff, Fees, Student, Parent, Attendance, Notification, BookRoom,Payment



@login_required(login_url='login')
def admin_dashboard(request):
    return render(request,'admin_temp/admin_dashboard.html')


@login_required(login_url='login')
def add_hostel(request):
    form = hostelform()
    if request.method == 'POST':
        form = hostelform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('viewhostel')
    return render(request, 'admin_temp/add_hostel.html', {'form': form})

@login_required(login_url='login')
def view_hostel(request):
    data = Hostel.objects.all()
    return render(request, 'admin_temp/view_hostel.html', {'data': data})

@login_required(login_url='login')
def update_hostel(request, id):
    n = Hostel.objects.get(id=id)
    if request.method == 'POST':
        form = hostelform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewhostel')
    else:
        form = hostelform(request.POST or None, instance=n)
    return render(request, 'admin_temp/add_hostel.html', {'form': form})

@login_required(login_url='login')
def delete_hostel(request, id=None):
    form = Hostel.objects.get(id=id)
    form.delete()
    return redirect('viewhostel')

@login_required(login_url='login')
def add_foods(request):
    form = foods()
    if request.method == 'POST':
        form = foods(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('viewfoods')
    return render(request, 'admin_temp/add_foods.html', {'form': form})

@login_required(login_url='login')
def view_food(request):
    data = Food.objects.all()
    return render(request, 'admin_temp/view_food.html', {'data': data})

@login_required(login_url='login')
def update_food(request, id):
    x = Food.objects.get(id=id)
    if request.method == 'POST':
        form = foods(request.POST or None, instance=x)
        if form.is_valid():
            form.save()
            return redirect('viewfoods')
    else:
        form = foods(request.POST or None, instance=x)
    return render(request, 'admin_temp/add_foods.html', {'form': form})

@login_required(login_url='login')
def delete_food(request, id=None):
    n = Food.objects.get(id=id)
    n.delete()
    return redirect('viewfoods')

@login_required(login_url='login')
def view_complaint(request):
    data = Complaint.objects.all()
    return render(request, 'admin_temp/view_complaint.html', {'data': data})

@login_required(login_url='login')
def add_staff(request):
    form = staffform()
    if request.method == 'POST':
        form = staffform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('viewstaff')
    return render(request, 'admin_temp/add_staff.html', {'form': form})

@login_required(login_url='login')
def view_staff(request):
    data = Staff.objects.all()
    return render(request, 'admin_temp/view_staff.html', {'data': data})

@login_required(login_url='login')
def update_staff(request, id):
    n = Staff.objects.get(id=id)
    if request.method == 'POST':
        form = staffform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewstaff')
    else:
        form = staffform(request.POST or None, instance=n)
    return render(request, 'admin_temp/add_staff.html', {'form': form})

@login_required(login_url='login')
def delete_staff(request, id=None):
    n = Staff.objects.get(id=id)
    n.delete()
    return redirect('viewstaff')

@login_required(login_url='login')
def add_fees(request):
    form = feesform()
    if request.method == 'POST':
        form = feesform(request.POST)
        if form.is_valid():
            bill = form.save(commit=False)
            bill_qs = Fees.objects.filter(student=bill.student, from_date=bill.from_date, to_date=bill.to_date)
            if bill_qs.exists():
                messages.info(request, 'bill already added for the student in this duration')
            else:
                bill.save()
                messages.info(request, 'bill added')
                return redirect('viewfees')
    return render(request, 'admin_temp/add_fees.html', {'form': form})

@login_required(login_url='login')
def load_bill(request):
    student_id = request.GET.get('studentId')
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    student = Student.objects.get(user_id=student_id)
    present_days = Attendance.objects.filter(student=student, date__range=[from_date, to_date]).count()
    amount = present_days * 200
    rent = 2000
    data = {
        'present_days': present_days,
        'mess_bill': amount,
        'room_rent': rent
    }
    return JsonResponse(data)

@login_required(login_url='login')
def add_attendance(request):
    student = Student.objects.filter(approval_status=True)
    return render(request, 'admin_temp/student_list.html', {'student': student})


now = datetime.datetime.now()

@login_required(login_url='login')
def mark(request, id):
    user = Student.objects.get(user_id=id)
    att = Attendance.objects.filter(student=user, date=datetime.date.today())
    if att.exists():
        messages.info(request, "Today's attendance already marked for this student")
        return redirect('view_attendances')
    else:
        if request.method == 'POST':
            attndc = request.POST.get('attendance')
            Attendance(student=user, date=datetime.date.today(), attendance=attndc, time=now.time()).save()
            messages.info(request, "attendance added successfully")
            return redirect('view_attendances')
    return render(request, 'admin_temp/mark_list.html')

@login_required(login_url='login')
def view_attendance(request):
    value_list = Attendance.objects.values_list('date', flat=True).distinct()
    attendances = {}
    for value in value_list:
        attendances[value] = Attendance.objects.filter(date=value)
    return render(request, 'admin_temp/view_attendance.html', {'attendances': attendances})

@login_required(login_url='login')
def day_attendance(request, date):
    attendance = Attendance.objects.filter(date=date)
    context = {
        'attendances': attendance,
        'date': date
    }
    return render(request, 'admin_temp/day_attendance.html', context)

@login_required(login_url='login')
def approve_student(request, id):
    student = Student.objects.get(user_id=id)
    student.approval_status = True
    student.save()
    messages.info(request, 'student approved successfully')
    return HttpResponseRedirect(reverse('viewstudent'))

@login_required(login_url='login')
def reject_student(request, id):
    student = Student.objects.get(user_id=id)
    if request.method == 'POST':
        student.approval_status = False
        student.save()
        messages.info(request, 'Reject student Registration')
        return redirect('viewstudent')
    return render(request, 'admin_temp/reject_student.html')

@login_required(login_url='login')
def approve_parent(request, id):
    parents = Parent.objects.get(user_id=id)
    parents.approval_status = True
    parents.save()
    messages.info(request, 'parent approved successfully')
    return HttpResponseRedirect(reverse('viewparent'))

@login_required(login_url='login')
def reject_parent(request, id):
    parents = Parent.objects.get(user_id=id)
    if request.method == 'POST':
        parents.approval_status = False
        parents.save()
        messages.info(request, 'Reject parent Registration')
        return redirect('viewparent')
    return render(request, 'admin_temp/parent_reject_student.html')

@login_required(login_url='login')
def view_fees(request):
    data = Fees.objects.all()
    return render(request, 'admin_temp/view_fees.html', {'data': data})

@login_required(login_url='login')
def view_student(request):
    data = Student.objects.all()
    return render(request, 'admin_temp/view_student.html', {'data': data})

@login_required(login_url='login')
def view_parent(request):
    data = Parent.objects.all()
    return render(request, 'admin_temp/view_parent.html', {'data': data})

@login_required(login_url='login')
def add_notification(request):
    form = notificationform()
    if request.method == 'POST':
        form = notificationform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'successfully added')
            return redirect('viewnotification')
    return render(request, 'admin_temp/add_notification.html', {'form': form})

@login_required(login_url='login')
def view_notification(request):
    data = Notification.objects.all()
    return render(request, 'admin_temp/view notification.html', {'data': data})


@login_required(login_url='login')
def delete_notification(request, id=None):
    n = Notification.objects.get(id=id)
    n.delete()
    return redirect('viewnotification')

@login_required(login_url='login')
def booking(request):
    book=BookRoom.objects.all()
    return render(request,'admin_temp/booking.html',{'book':book})

@login_required(login_url='login')
def confirm_booking(request,id):
    details_qs=Hostel.objects.all()
    if details_qs.exists():
        book=BookRoom.objects.get(id=id)
        book.status=1
        book.save()
        hstl=Hostel.objects.all().last()
        occupied=hstl.occupied
        hstl.occupied=int(occupied)-1
        hstl.save()
        messages.info(request,'room booking confirmed')
        return redirect('booking')
    else:
        messages.info(request,'please update hostel details')
        return HttpResponseRedirect(reverse('booking'))

@login_required(login_url='login')
def reject_booking(request,id):
    book=BookRoom.objects.get(id=id)
    if request.method=='POST':
        book.status=2
        book.save()
        messages.info(request,'room booking rejected')
        return redirect('booking')
    return render(request,'admin_temp/reject_booking.html')

@login_required(login_url='login')
def reply_complaint(request, id):
    c = Complaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        c.reply = r
        c.save()
        messages.info(request, 'Reply send for complaint')
        return redirect('viewcomplaint')
    return render(request, 'admin_temp/reply_complaint.html', {'c': c})


@login_required(login_url='login')
def view_payment(request):
    payment=Fees.objects.filter(status=1)
    return render(request,'admin_temp/view_payment.html',{'payment':payment})


