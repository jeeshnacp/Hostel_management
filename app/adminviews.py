from django.contrib import messages
from django.shortcuts import render, redirect

from app.form import hostelform
from app.models import hostel


def add_hostel(request):
    form=hostelform()
    if request.method=='POST':
        form=hostelform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'successfully added')
            return redirect('admin_home')
    return render(request,'add_hostel.html',{'form':form})

def view_hostel(request):
    data=hostel.objects.all()
    return render(request,'view_hostel.html',{'data':data})
