from django.shortcuts import render

from app.models import Hostel, Food, Staff


def view_hostel(request):
    data=Hostel.objects.all()
    return render(request,'parent_temp/parent_view_hostel.html',{'data':data})

def view_food(request):
    data=Food.objects.all()
    return render(request,'parent_temp/parent_view_food.html',{'data':data})

def view_staff(request):
    data=Staff.objects.all()
    return render(request,'parent_temp/parent_view_staff.html',{'data':data})
