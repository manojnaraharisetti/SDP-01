from imp import source_from_cache
from tokenize import Name
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
import datetime
from .models import event,catering,Musicalconcertm,weddinghalls

def dealerlogin(request):
    return render(request ,"login2.html")

def dealerregister(request):
    return render(request , "register2.html")

def userlogin(request):
    return render(request ,"login.html")

def userregister(request):
    return render(request , "register.html")

def home(request):
    return render(request,'home.html')

def dealerhome(request):
    return render(request,'dealerhome.html')
def history(request):
    allevents = event.objects.all()
    context = {'al':allevents}
    return render(request,'history.html',context)

def faqs(request):
    return render(request,'faqs.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def calender(request):
    return render(request,'calender.html')

def weddinghall(request):
    return render(request ,"weddinghall.html")

def cateringservice(request):
    return render(request ,'caterings.html')

def Musicalconcert(request):
    return render(request ,"Musicconcerts.html")

def userloginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        user1 = auth.authenticate(username=username, password=password)
        print(username, password)
        if user1 is not None:
            auth.login(request,user1)
            return redirect('/home')
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/userlogin")
    else:
        return render(request,'login.html')


def dealerloginuser(request):
    if request.method == 'POST':
        username1 = request.POST['username']
        password1 = request.POST['passwd']
        user2 = auth.authenticate(username=username1, password=password1)
        print(username1, password1)
        if user2 is not None:
            if user2.is_staff == True: 
                auth.login(request,user2)
                return redirect('/dealerhome')
            messages.info(request, 'invalid username or password')
            return redirect("/dealerlogin")
        else:
            messages.info(request, 'invalid username or password')
            return redirect("/dealerlogin")
    else:
        return render(request,'login2.html')

def dash(request):
    return render(request,'dash.html')
def userregisteruser(request):
    if request.method == 'POST':
        fname = request.POST['fn']
        lname = request.POST['ln']
        email = request.POST['email']
        username = request.POST['uname']
        passwd = request.POST['password']
        messages.info(request, 'username already exists')
        date = datetime.date.today()
        user3 = User.objects.create_user(first_name = fname, last_name = lname, username = username , password = passwd , email = email, date_joined = date)
        user3.save()
        print('user created')
        return redirect('/userlogin')

    return render(request,'login.html')

def dealerregisteruser(request):
    if request.method == 'POST':
        fname = request.POST['fn']
        lname = request.POST['ln']
        email = request.POST['email']
        username = request.POST['uname']
        passwd = request.POST['password']
        messages.info(request, 'Passwords dont match')
        date = datetime.date.today()
        user = User.objects.create_user(first_name = fname, last_name = lname, username = username , password = passwd, email = email, date_joined = date,is_staff=True)
        user.save()
        print('user created')
        return redirect('/dealerlogin')

    return render(request,'login2.html')


def event1(request):
    if request.method == 'POST':
        typeofevent=request.POST['tp']
        Name = request.POST['name']
        Date = str(request.POST['date'])
        starttime = str(request.POST['stime'])
        endtime = str(request.POST['etime'])
        venue = request.POST['venue']
        food = request.POST['food']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        print(typeofevent,Name,Date,starttime,endtime,venue,food,username)
        book = event(type=typeofevent,cname=Name,cdate=Date,cstime=starttime,cetime=endtime,cvenue=venue,cfood=food,username=username)
        book.save()
    return render(request,'event.html')
    
   

def Catering(request):
    if request.method == 'POST':
        Servicename=request.POST['catername']
        Name1=request.POST['catername1']
        PPrice=request.POST['caterprice']
        Mobile=request.POST['caternum']
        Email=request.POST['cateremail']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        print(Servicename,Name1,PPrice,Mobile,Email,username)
        cat = catering(sname=Servicename,namemanu=Name1,pricemanu=PPrice,mobile=Mobile,emailmanu=Email,username=username)
        cat.save()
        
         

    return render(request,'caterings.html')

def MusicConcerts(request):
    if request.method == 'POST':
         cname=request.POST['bnames']
         Name=request.POST['namel']
         address=request.POST['address1']
         City=request.POST['citys']
         poscode=request.POST['codes']
         totprice=request.POST['price']
         Mobile=request.POST['nums']
         Email=request.POST['email2']
         if request.user.is_authenticated:
            username = request.user.username
         print(cname,Name,address,City,poscode,totprice,Mobile,Email,username)
         Music = Musicalconcertm(conname=cname,name=Name,Address=address,City=City,pcode=poscode,Tprice=totprice,mobile=Mobile,email=Email,username=username)
         Music.save()

    return render(request,'Musicconcerts.html')

def weddinghall1(request):
    if request.method == 'POST':
         cname=request.POST['bname']
         Name=request.POST['name']
         address=request.POST['address']
         City=request.POST['city']
         poscode=request.POST['code']
         totprice=request.POST['price']
         Mobile=request.POST['num']
         Email=request.POST['emails']
         if request.user.is_authenticated:
            username = request.user.username
         print(cname,Name,address,City,poscode,totprice,Mobile,Email,username)
         weddinghall1 = weddinghalls(wname=cname,name=Name,Address=address,City=City,pcode=poscode,price=totprice,mobile=Mobile,email=Email,username=username)
         weddinghall1.save()

    return render(request,'weddinghall.html')






