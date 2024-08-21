from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request , 'html/login.html')

def register(request):
    return render(request , 'html/register.html')

def home(request):
    return render(request , 'html/home.html')

def contact(request):
    return render(request , 'html/contactus.html')

def about(request):
    return render(request , 'html/aboutus.html')

def lib(request):
    return render(request , 'html/lib.html')

def profile(request):
    return render(request , 'html/profile.html')

def fb(request):
    return render(request , 'html/fb.html')
