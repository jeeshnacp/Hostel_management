from django.urls import path

from app import views

urlpatterns = [
    path('login',views.login_view,name='login'),
    path('home',views.home,name='home')

]