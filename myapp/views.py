from django.shortcuts import render
from .models import Introduction
# Create your views here.

def home(request):
    intross=Introduction.objects.all()
    
    return render(request, 'home.html',{'intross': intross})

def books(request):
    return render(request, 'books.html')

def business(request):
    return render(request, 'business.html')

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    return render(request, 'courses.html')