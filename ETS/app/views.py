
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def login(request):
    return render(request ,"login.html")

def register(request):
    return render(request , "register.html")

def home(request):
    return render(request,'home.html')
def history(request):
    return render(request,'history.html')


def faqs(request):
    return render(request,'faqs.html')

def event(request):
    return render(request,'event.html')

def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')

