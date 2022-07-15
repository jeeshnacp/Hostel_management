from django.urls import path

from app import views, adminviews, studentviews, parentviews

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name='about'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('parent_home', views.parent_home, name='parent_home'),
    path('student_home', views.student_home, name='student_home'),
    path('student', views.student_register, name='student'),
    path('parent', views.parent_register, name='parent'),
    path('logout', views.logout_view, name='logout'),

    #admin

    path('dashboard', adminviews.admin_dashboard, name='dashboard'),
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
    path('booking',adminviews.booking,name='booking'),
    path('confirm/<int:id>/',adminviews.confirm_booking,name='confirm'),
    path('reject/<int:id>/',adminviews.reject_booking,name='reject'),
    path('reply_complaint/<int:id>/',adminviews.reply_complaint,name='reply_complaint'),
    path('view_payment',adminviews.view_payment,name='view_payment'),

    #student

    path('dashboard2', studentviews.student_dashboard, name='dashboard2'),
    path('studentviewhostel',studentviews.view_hostel,name='studentviewhostel'),
    path('studentviewfoods',studentviews.view_food,name='studentviewfoods'),
    path('studentcomplaint',studentviews.register_complaint,name='studentcomplaint'),
    path('view_attend', studentviews.view_attendance, name='view_attend'),
    path('profile',studentviews.view_profile,name='profile'),
    path('profile_update', studentviews.update_profile,name='profile_update'),
    path('room_booking', studentviews.book_room,name='room_booking'),
    path('booking_status', studentviews.booking_status,name='booking_status'),
    path('delete_profile', studentviews.delete_profile,name='delete_profile'),
    path('cancelbooking',studentviews.cancel_booking,name='cancelbooking'),
    path('payment',studentviews.payment_details,name='payment'),
    path('fees_details',studentviews.view_fee,name='fees_details'),
    path('view_complaint',studentviews.view_complaint,name='view_complaint'),
    path('do_payment/<int:id>/',studentviews.do_payment,name='do_payment'),
    path('view_payments',studentviews.view_payment,name='view_payments'),

    #parent

    path('dashboard1', parentviews.parent_dashboard, name='dashboard1'),
    path('parentviewhostel', parentviews.view_hostel, name='parentviewhostel'),
    path('parentviewfoods', parentviews.view_food, name='parentviewfoods'),
    path('viewattendance',parentviews.view_attendance,name='viewattendance'),
    path('delete_account', parentviews.delete_account, name='delete_account'),
    path('view_payments', parentviews.view_payments, name='view_payments'),

]