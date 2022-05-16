from django.contrib import messages
from django.shortcuts import render, redirect

from app.form import hostelform, foods
from app.models import hostel, food


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