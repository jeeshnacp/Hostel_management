from django.contrib import messages
from django.shortcuts import render, redirect

from app.form import hostelform, foods, staffform
from app.models import hostel, food, complaint, staff


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

