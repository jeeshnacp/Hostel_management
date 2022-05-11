from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

def home(request):
    return render(request,'home.html')


# Create your views here.
def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
               return redirect('admin_home')
            elif user.is_parent:
                return  redirect('parent_home')
            elif user.is_student:
                return redirect('student_home')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')