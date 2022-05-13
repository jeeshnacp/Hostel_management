from django.urls import path

from app import views, adminviews

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('',views.home,name='home'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('student',views.student_registration,name='student'),
    path('hostel',adminviews.view_hostel,name='hostel'),
    path('addhostel',adminviews.add_hostel,name='addhostel'),

]