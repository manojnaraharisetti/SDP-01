import datetime
from tokenize import Name
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Registerpg


def login(request):
    return render(request ,"login.html")

'''def login2(request):
    return render(request ,"login2.html")'''
def register(request):
    return render(request , "register.html")
def home(request):
    return render(request,'home.html')

'''def register2(request):
    return render(request , "register2.html")'''


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

def calender(request):
    return render(request,'calender.html')
#def home2(request):
   # return render(request,'home2.html')

def loginuser(request):
    mail = request.POST['email']
    passwd = request.POST['password']

def dash(request):
    return render(request,'dash.html')
def registeruser(request):
    if request.method == 'POST':
        fname = request.POST['fn']
        lname = request.POST['ln']
        email = request.POST['email']
        username = request.POST['uname']
        passwd = request.POST['password']
        messages.info(request, 'Passwords dont match')
        date = datetime.date.today()
        user = User.objects.create_user(first_name = fname, last_name = lname, username = username , password = passwd , email = email, date_joined = date)
        user.save()
        print('user created')
        return redirect('/login')

    return render(request,'login.html')


'''def registeruser2(request):
    Name = request.POST['name']
    entered_password = request.POST['password']
    email = request.POST['email']
    dob = request.POST['dob']
    companyname=request.POST['org']
    print(Name, entered_password, email, dob)
    client = MongoClient('mongodb://localhost:27017/')
    db = client['ETS-1']  # database name
    info = db.SDP
    n = {"Name": Name,
         "password": entered_password,
         " organization":companyname,
         "email": email,
         "dob": dob
         }
    tofind1 = {"email": email}
    user = db.user
    c = 0
    for x in tofind1:
        if (user.find_one(tofind1)):
            c = 1
    if request.method == "POST":
        if c == 1:
            messages.warning(request, "Email already exists")
        elif Name == "":
            messages.warning(request, "Enter Name")
        elif dob == "":
            error = "Enter DOB"
        elif entered_password == "":
            error = "Enter Password"
        elif email == "":
            error = "Enter Email"
        else:
            user.insert_one(n)
            return redirect('/login2')
    return redirect('/register2')

def loginuser2(request):
    mail = request.POST['email']
    passwd = request.POST['password']
    client = MongoClient('mongodb://localhost:27017/')
    db = client['ETS-1']  # database name
    info = db.SDP
    user = db.user
    m = 0
    p = 0
    t1 = {"email": mail}
    for x in t1:
        if (user.find_one(t1)):
            m = 1
    t2 = {"password": passwd}
    for x in t2:
        if (user.find_one(t2)):
            p = 1
    if request.method == "POST":
        if p != 1 and m != 1:
            error = "Please Register"
        elif m != 1:
            error = "Please Register"
        elif p != 1:
            error = "Invalid Password"
        else:
            return redirect('/home2')
    return redirect('/login2')'''


