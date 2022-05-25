import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from app.form import hostelform, foods, staffform, feesform
from app.models import hostel, food, complaint, staff, fees, student, parent, attendance


def add_hostel(request):
    form=hostelform()
    if request.method=='POST':
        form=hostelform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'successfully added')
            return redirect('viewhostel')
    return render(request,'admin_temp/add_hostel.html',{'form':form})

def view_hostel(request):
    data=hostel.objects.all()
    return render(request,'admin_temp/view_hostel.html',{'data':data})

def update_hostel(request,id):
    n=hostel.objects.get(id=id)
    if request.method=='POST':
        form=hostelform(request.POST or None,instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewhostel')
    else:
        form=hostelform(request.POST or None,instance=n)
    return render(request,'admin_temp/add_hostel.html',{'form':form})


def delete_hostel(request,id=None):
    form=hostel.objects.get(id=id)
    form.delete()
    return redirect('viewhostel')


def add_foods(request):
    form=foods()
    if request.method=='POST':
        form=foods(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'successfully added')
            return redirect('viewfoods')
    return render(request,'admin_temp/add_foods.html',{'form':form})

def view_food(request):
    data=food.objects.all()
    return render(request,'admin_temp/view_food.html',{'data':data})


def update_food(request,id):
    x=food.objects.get(id=id)
    if request.method=='POST':
        form=foods(request.POST or None,instance=x)
        if form.is_valid():
            form.save()
            return redirect('viewfoods')
    else:
        form=foods(request.POST or None,instance=x)
    return render(request,'admin_temp/add_foods.html',{'form':form})

def delete_food(request,id=None):
    n=food.objects.get(id=id)
    n.delete()
    return redirect('viewfoods')

def view_complaint(request):
    data=complaint.objects.all()
    return render(request,'admin_temp/view_complaint.html',{'data':data})

def add_staff(request):
    form=staffform()
    if request.method=='POST':
        form=staffform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'successfully added')
            return redirect('viewstaff')
    return render(request,'admin_temp/add_staff.html',{'form':form})

def view_staff(request):
    data=staff.objects.all()
    return render(request,'admin_temp/view_staff.html',{'data':data})

def update_staff(request,id):
    n=staff.objects.get(id=id)
    if request.method=='POST':
        form=staffform(request.POST or None,instance=n)
        if form.is_valid():
            form.save()
            return redirect('viewstaff')
    else:
        form=staffform(request.POST or None,instance=n)
    return render(request,'admin_temp/add_staff.html',{'form':form})


def delete_staff(request,id=None):
    n=staff.objects.get(id=id)
    n.delete()
    return redirect('viewstaff')


def add_fees(request):
    form=feesform()
    if request.method=='POST':
        form=feesform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('viewfees')
    return render(request,'admin_temp/add_fees.html',{'form':form})

def add_attendance(request):
    students=student.objects.filter(approval_status=True)
    return render(request,'admin_temp/student_list.html',{'students':students})


now=datetime.datetime.now()
def mark(request,id):
    user=student.objects.get(user_id=id)
    att=attendance.objects.filter(student=user,date=datetime.date.today())
    if att.exists():
        messages.info(request,"Today's attendance already marked for this student")
        return redirect('addattendance')
    else:
        if request.method=='POST':
            attndc=request.POST.get('attendance')
            attendance(student=user,date=datetime.date.today(),attendance=attndc,time=now.time()).save()
            messages.info(request,"attendance added successfully")
            return redirect('addattendance')
    return render(request,'admin_temp/mark_attendance.html')


def approve_student(request,id):
    students=student.objects.get(user_id=id)
    students.approval_status=True
    students.save()
    messages.info(request,'student approved successfully')
    return HttpResponseRedirect(reverse('view_registration_details'))

def reject_student(request,id):
    students=student.objects.get(user_id=id)
    if request.method=='POST':
        students.approval_status==False
        student.save()
        messages.info(request,'Reject student Registration')
        return redirect('student')
    return render(request,'reject_student.html')



def view_fees(request):
    data=fees.objects.all()
    return render(request,'admin_temp/view_fees.html',{'data':data})

def view_student(request):
    data=student.objects.all()
    return render(request,'admin_temp/view_student.html',{'data':data})

def view_parent(request):
    data=parent.objects.all()
    return render(request,'admin_temp/view_parent.html',{'data':data})


