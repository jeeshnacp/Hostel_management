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
    path('updatehostel/<int:id>/',adminviews.update_hostel,name='updatehostel'),
    path('deletehostel/<int:id>/',adminviews.delete_hostel,name='deletehostel'),
    path('addfoods', adminviews.add_foods, name='addfoods'),
    path('viewfoods', adminviews.view_food, name='viewfoods'),
    path('updatefood/<int:id>/',adminviews.update_food,name='updatefood'),
    path('deletefood/<int:id>/',adminviews.delete_food,name='deletefood'),
    path('viewcomplaint',adminviews.view_complaint,name='viewcomplaint'),
    path('addstaff',adminviews.add_staff,name='addstaff'),
    path('viewstaff',adminviews.view_staff,name='viewstaff'),
    path('updatestaff/<int:id>/', adminviews.update_staff, name='updatestaff'),
    path('deletestaff/<int:id>/', adminviews.delete_staff, name='deletestaff'),
    path('addfees',adminviews.add_fees,name='addfees'),
    path('viewfees',adminviews.view_fees,name='viewfees'),
    path('viewstudent',adminviews.view_student,name='viewstudent'),
    path('viewparent',adminviews.view_parent,name='viewparent'),
    path('addattendance',adminviews.add_attendance,name='addattendance'),
    path('mark/<int:id>/',adminviews.mark,name='mark'),
    path('approve_student/<int:id>/',adminviews.approve_student,name='approve_student'),
    path('reject_student/<int:id>/',adminviews.reject_student,name='reject_student'),
    path('approve_parent/<int:id>/', adminviews.approve_parent, name='approve_parent'),
    path('reject_parent/<int:id>/', adminviews.reject_parent, name='reject_parent'),
    path('view_attendances',adminviews.view_attendance,name='view_attendances'),
    path('day_attendances/<date>/',adminviews.day_attendance,name='day_attendances'),
    path('ajax/loadbill',adminviews.load_bill,name='ajax_load_bill'),
    path('addnotification', adminviews.add_notification, name='addnotification'),
    path('viewnotification', adminviews.view_notification, name='viewnotification'),
    path('deletenotification/<int:id>/', adminviews.delete_notification, name='deletenotification'),

    path('studentviewhostel',studentviews.view_hostel,name='studentviewhostel'),
    path('studentviewfoods',studentviews.view_food,name='studentviewfoods'),
    path('studentcomplaint',studentviews.register_complaint,name='studentcomplaint'),

    path('parentviewhostel', parentviews.view_hostel, name='parentviewhostel'),
    path('parentviewfoods', parentviews.view_food, name='parentviewfoods'),
    path('parentviewstaff',parentviews.view_staff,name='parentviewstaff'),

]