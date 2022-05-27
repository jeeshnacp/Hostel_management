from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from app.form import loginRegister, studentregister, parentregister


def home(request):
    return render(request, 'home.html')


def admin_home(request):
    return render(request, 'admin_temp/admin_home.html')


def parent_home(request):
    return render(request, 'parent_temp/parent_home.html')


def student_home(request):
    return render(request, 'student_temp/student_home.html')


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_home')
        elif user is not None and user.is_parent:
            if user.parent.approval_status == True:
                login(request, user)
                return redirect('parent_home')
            else:
                messages.info(request, 'you are not approval to login')
        elif user is not None and user.is_student:
            if user.student.approval_status == True:
                login(request, user)
                return redirect('student_home')
            else:
                messages.info(request, 'you are not approval to login')
        else:
            messages.info(request, 'invalid credentials')

    return render(request, 'login.html')


def student_register(request):
    student_form = studentregister()
    login_form = loginRegister()
    if request.method == 'POST':
        student_form = studentregister(request.POST, request.FILES)
        login_form = loginRegister(request.POST)
        if student_form.is_valid() and login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_student = True
            user.save()
            student = student_form.save(commit=False)
            student.user = user
            student.save()
            messages.info(request, 'student Registration Successfully')
            return redirect('login')

    return render(request, 'student_registration.html', {'login_form': login_form, 'student_form': student_form})


def parent_register(request):
    parent_form = parentregister()
    login_form = loginRegister()
    if request.method == 'POST':
        parent_form = parentregister(request.POST)
        login_form = loginRegister(request.POST)
        if parent_form.is_valid() and login_form.is_valid():
            user = login_form.save(commit=False)
            user.is_parent = True
            user.save()
            parent = parent_form.save(commit=False)
            parent.user = user
            parent.save()
            messages.info(request, 'parent Registration Successfully')
            return redirect('login')

    return render(request, 'parent_registration.html', {'login_form': login_form, 'parent_form': parent_form})


def logout_view(request):
    logout(request)
    return redirect('login')
