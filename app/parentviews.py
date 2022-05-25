from django.shortcuts import render

from app.models import hostel, food, staff


def view_hostel(request):
    data=hostel.objects.all()
    return render(request,'parent_temp/parent_view_hostel.html',{'data':data})

def view_food(request):
    data=food.objects.all()
    return render(request,'parent_temp/parent_view_food.html',{'data':data})

def view_staff(request):
    data=staff.objects.all()
    return render(request,'parent_temp/parent_view_staff.html',{'data':data})
