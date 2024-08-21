from django.contrib import admin
from django.urls import include ,path
from . import views

urlpatterns = [
    path('' , views.login , name='login'),
    path('register' , views.register , name='register'),
    path('about' , views.about , name='about'),
    path('contact' , views.contact , name='contact'),
    path('profile' , views.profile, name='profile'),
    path('home' , views.home , name='home'),
    path('lib' , views.lib, name='lib'),
   
    
]