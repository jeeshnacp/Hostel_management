from django.urls import path

from app import views, adminviews, studentviews, parentviews

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('',views.home,name='home'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('parent_home', views.parent_home, name='parent_home'),
    path('student_home', views.student_home, name='student_home'),
    path('student', views.student_register, name='student'),
    path('parent', views.parent_register, name='parent'),
    path('logout', views.logout_view, name='logout'),

    path('viewhostel',adminviews.view_hostel,name='viewhostel'),
    path('addhostel',adminviews.add_hostel,name='addhostel'),
    path('addfoods', adminviews.add_foods, name='addfoods'),
    path('viewfoods', adminviews.view_food, name='viewfoods'),


    path('studentviewhostel',studentviews.view_hostel,name='studentviewhostel'),
    path('studentviewfoods',studentviews.view_food,name='studentviewfoods'),




    path('parentviewhostel', parentviews.view_hostel, name='parentviewhostel'),
    path('parentviewfoods', parentviews.view_food, name='parentviewfoods'),

]