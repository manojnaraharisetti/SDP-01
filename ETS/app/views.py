from imp import source_from_cache
from tokenize import Name
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
import datetime
from .models import event,catering,contact1,dcontact,Musicalconcertm,weddinghalls,BirthdayParty
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

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
def terms(request):
    return render(request,"termsandconditions1.html")
def terms1(request):
    if request.user.is_authenticated:
        return render(request,"termsandconditions.html")
    messages.success(request,"Please Login")
    return redirect("/")
def terms2(request):
    if request.user.is_authenticated:
        return render(request,"termsandconditions2.html")
    messages.success(request,"Please Login")
    return redirect("/dealerhome")
def terms3(request):
    return render(request,"termsandconditions3.html")

def history(request):
    if request.user.is_authenticated:
        username=request.user.username
        allevents = event.objects.filter(username=username)
        context = {'al': allevents}
        return render(request, 'history.html', context)
    messages.success(request,"Please login")
    return redirect('/')

def deleteevent(request):
    if request.method == 'POST':
        cname = request.POST['name']
        type = request.POST['event']
        cdate=request.POST['date']
        if request.user.is_authenticated:
            username = request.user.username
            if event.objects.filter(cname=cname).exists() and event.objects.filter(cdate=cdate).exists():
                userdata = event.objects.filter(username=username,cname=cname,type=type,cdate=cdate)
                userdata.delete()
                messages.success(request,'Event deleted Sucessfully')
                return render(request,'delete.html')
            messages.success(request,"Data doesnot exists")
            return render(request,'delete.html')
    if request.user.is_authenticated:
        return render(request, 'delete.html')
    else:
        messages.success(request, "PLEASE LOGIN!")
    return redirect('/')

def dealerdeleteevent(request):
    if request.method == 'POST':
        cname = request.POST['cname']
        type = request.POST['event']
        oname=request.POST['oname']
        if request.user.is_authenticated:
            if type == "Caterings":
                username = request.user.username
                if catering.objects.filter(sname=cname).exists() and catering.objects.filter(namemanu=oname).exists():
                    userdata = catering.objects.filter(username=username, sname=cname, type=type, namemanu=oname)
                    print(userdata)
                    userdata.delete()
                    messages.success(request, 'Event deleted Sucessfully')
                    return render(request, 'dealerdelete.html')
                messages.success(request,"Data doesnot exists")
                return render(request,'dealerdelete.html')
            if type == "Musicical concert":
                username = request.user.username
                if Musicalconcertm.objects.filter(conname=cname).exists() and Musicalconcertm.objects.filter(name=oname).exists():  
                    userdata1 = Musicalconcertm.objects.filter(username=username, conname=cname, type1=type, name=oname)
                    print(userdata1)
                    userdata1.delete()
                    messages.success(request, 'Event deleted Sucessfully')
                    return render(request, 'dealerdelete.html')
                messages.success(request,"Data doesnot exists")
                return render(request,'dealerdelete.html')
            if type == "Wedding Hall":
                username = request.user.username
                if weddinghalls.objects.filter(wname=cname).exists() and weddinghalls.objects.filter(name=oname).exists():
                    userdata2 = weddinghalls.objects.filter(username=username, wname=cname, type2=type, name=oname)
                    userdata2.delete()
                    messages.success(request, 'Event deleted Sucessfully')
                    return render(request, 'dealerdelete.html')
                messages.success(request,"Data doesnot exists")
                return render(request,'dealerdelete.html')
            if type == "Birthday Party":
                username = request.user.username
                if BirthdayParty.objects.filter(birthdayname=cname).exists() and BirthdayParty.objects.filter(birthdayame=oname).exists(): 
                    userdata3= BirthdayParty.objects.filter(username=username, birthdayname=cname, type3=type, birthdayame=oname)
                    userdata3.delete()
                    messages.success(request, 'Event deleted Sucessfully')
                    return render(request, 'dealerdelete.html')
                messages.success(request,"Data doesnot exists")
                return render(request,'dealerdelete.html')
    if request.user.is_authenticated:
        return render(request, 'dealerdelete.html')
    else:
        messages.success(request, "PLEASE LOGIN!")
    return redirect('/')




def dealerhistory(request):
    if request.user.is_authenticated:
        username0=request.user.username
        allevent = catering.objects.filter(username=username0)
        cont = {'bl': allevent}
        return render(request, 'cateringdealerhistory.html', cont)

    messages.success(request,"Please login")
    return redirect('/')

def dealerhistory1(request):
    if request.user.is_authenticated:
        username1=request.user.username
        allevent1 = Musicalconcertm.objects.filter(username=username1)
        cont1 = {'cl': allevent1}
        return render(request, 'Musicdealerhistory.html',cont1)

    messages.success(request,"Please login")
    return redirect('/')

def dealerhistory2(request):
    if request.user.is_authenticated:
        username2=request.user.username
        allevent2 = weddinghalls.objects.filter(username=username2)
        cont1 = {'dl': allevent2}
        return render(request, 'Weddingdealerhistory.html',cont1)

    messages.success(request,"Please login")
    return redirect('/')


def dealerhistory3(request):
    if request.user.is_authenticated:
        username3=request.user.username
        allevent3 = BirthdayParty.objects.filter(username=username3)
        cont1 = {'el': allevent3}
        return render(request, 'Birthdaydealerhistory.html',cont1)

    messages.success(request,"PLEASE LOGIN!")
    return redirect('/')



def dealerhistory00(request):
    if request.user.is_authenticated:
        username0=request.user.username
        allevent = catering.objects.filter(username=username0)
        cont = {'bl': allevent}
        return render(request, 'cateringdealerhistory.html', cont)

    messages.success(request,"Please login")
    return redirect('/dealerhome')

def dealerhistory01(request):
    if request.user.is_authenticated:
        username1=request.user.username
        allevent1 = Musicalconcertm.objects.filter(username=username1)
        cont1 = {'cl': allevent1}
        return render(request, 'Musicdealerhistory.html',cont1)

    messages.success(request,"Please login")
    return redirect('/dealerhome')

def dealerhistory02(request):
    if request.user.is_authenticated:
        username2=request.user.username
        allevent2 = weddinghalls.objects.filter(username=username2)
        cont1 = {'dl': allevent2}
        return render(request, 'Weddingdealerhistory.html',cont1)

    messages.success(request,"Please login")
    return redirect('/dealerhome')


def dealerhistory03(request):
    if request.user.is_authenticated:
        username3=request.user.username
        allevent3 = BirthdayParty.objects.filter(username=username3)
        cont1 = {'el': allevent3}
        return render(request, 'Birthdaydealerhistory.html',cont1)

    messages.success(request,"PLEASE LOGIN!")
    return redirect('/dealerhome')

def faqs(request):
    return render(request,'faqs.html')

def dfaqs(request):
    return render(request,'dealerfaqs.html')

def contact(request):
    return render(request,'contact.html')

def dealercontacts(request):
    return render(request,'dealercontact.html')

def about(request):
    return render(request,'about.html')

def dabout(request):
    return render(request,'dealerabout.html')

def cateringbook(request):
    if request.user.is_authenticated:
        allevent1 = catering.objects.all()
        cont1 = {'kl': allevent1}
        return render(request, 'cateringbook.html',cont1)
    messages.success(request, "PLEASE LOGIN!")
    return redirect('/')

def Musicbook(request):
    if request.user.is_authenticated:
       allevent2 = Musicalconcertm.objects.all()
       cont2 = {'pl': allevent2}
       return render(request, 'concertbook.html',cont2)
    messages.success(request, "PLEASE LOGIN!")
    return redirect('/')

def Birthdaybook(request):
    if request.user.is_authenticated:
        allevent4 = BirthdayParty.objects.all()
        cont4 = {'il': allevent4}
        return render(request, 'birthdaybook.html',cont4)
    messages.success(request, "PLEASE LOGIN!")
    return redirect('/')

def weddingbook(request):
    if request.user.is_authenticated:
        allevent3 = weddinghalls.objects.all()
        cont3 = {'ol': allevent3}
        return render(request, 'weddingbook.html',cont3)
    messages.success(request, "PLEASE LOGIN!")
    return redirect('/')
    
def userloginuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['passwd']
        user1 = auth.authenticate(username=username, password=password)
        print(username, password)
        if user1 is not None:
            auth.login(request,user1)
            messages.success(request,"successfully logged in" )
            return redirect('/home')
        else:
            messages.success(request,"Authentication failed Please Login Again")
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
                messages.success(request,"successfully logged in" )
                return redirect('/dealerhome')
        else:
            messages.success(request,"Authentication failed Please Login Again")
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
            date = datetime.date.today()
            if User.objects.filter(username=username).exists():
                messages.success(request,"Username already exists")
                return redirect('/userregister')
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
        date = datetime.date.today()
        if User.objects.filter(username=username).exists():
            messages.success(request,"Username already exists")
            return redirect('/dealerregister')
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
        selectdealer = request.POST['sdeal']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        if starttime == endtime:
            messages.success(request,"Both times should not be equal")
            return redirect('/event')
        print(typeofevent,Name,Date,starttime,endtime,venue,food,selectdealer)
        book = event(type=typeofevent,cname=Name,cdate=Date,cstime=starttime,cetime=endtime,cvenue=venue,cfood=food,sdealer=selectdealer,username=username)
        book.save()
        msg = "Your Event has been successfully booked"+"\n\n\n"+"EVENT DEATILS :"+"\n\n"+"Event Name :"+typeofevent+"\n"+"Name :"+Name+"\n"+"Date :"+Date+"\n"+"Your Dealer  Service Name :"+selectdealer+"\n"
        send_mail('Event Confirmation',  # subject
                  msg,
                  'outlining25@gmail.com',  # from
                   [request.user.email],  # to
                  fail_silently=False,
                  )

        messages.success(request,"Event is successfuly Booked !verify your mail" )
        return render(request,'event.html')
    if request.user.is_authenticated:
        allevent4 = catering.objects.all()
        cont4 = {'il': allevent4}
        return render(request,'event.html',cont4)
    else:
         messages.success(request, "PLEASE LOGIN!")
    return redirect('/')


def event2(request):
    if request.method == 'POST':
        typeofevent = request.POST['tp']
        Name = request.POST['name']
        Date = str(request.POST['date'])
        starttime = str(request.POST['stime'])
        endtime = str(request.POST['etime'])
        venue = request.POST['venue']
        food = request.POST['food']
        selectdealer = request.POST['sdeal']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        if starttime == endtime:
            messages.success(request, "Both times should not be equal")
            return redirect('/event1')
        print(typeofevent, Name, Date, starttime, endtime, venue, food,selectdealer)
        book = event(type=typeofevent, cname=Name, cdate=Date, cstime=starttime, cetime=endtime, cvenue=venue,
                     cfood=food,sdealer=selectdealer, username=username)
        book.save()
        msg = "Your Event has been successfully booked"+"\n\n\n"+"EVENT DEATILS :"+"\n\n"+"Event Name :"+typeofevent+"\n"+"Name :"+Name+"\n"+"Date :"+Date+"\n"+"Your Dealer  Service Name :"+selectdealer+"\n"
        send_mail('Event Confirmation',  # subject
                  msg,
                  'outlining25@gmail.com',  # from
                  [request.user.email],  # to
                  fail_silently=False,
                  )

        messages.success(request, "Event is successfuly Booked !verify your mail")
        return render(request, 'event1.html')
    if request.user.is_authenticated:
        allevent4 = Musicalconcertm.objects.all()
        cont4 = {'il': allevent4}
        return render(request, 'event1.html',cont4)
    else:
        messages.success(request, "PLEASE LOGIN!")
    return redirect('/')


def event3(request):
    if request.method == 'POST':
        typeofevent = request.POST['tp']
        Name = request.POST['name']
        Date = str(request.POST['date'])
        starttime = str(request.POST['stime'])
        endtime = str(request.POST['etime'])
        venue = request.POST['venue']
        food = request.POST['food']
        selectdealer = request.POST['sdeal']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        if starttime == endtime:
            messages.success(request, "Both times should not be equal")
            return redirect('/event2')
        print(typeofevent, Name, Date, starttime, endtime, venue, food,selectdealer)
        book = event(type=typeofevent, cname=Name, cdate=Date, cstime=starttime, cetime=endtime, cvenue=venue,
                     cfood=food,sdealer=selectdealer, username=username)
        book.save()
        msg = "Your Event has been successfully booked"+"\n\n\n"+"EVENT DEATILS :"+"\n\n"+"Event Name :"+typeofevent+"\n"+"Name :"+Name+"\n"+"Date :"+Date+"\n"+"Your Dealer  Service Name :"+selectdealer+"\n"
        send_mail('Event Confirmation',  # subject
                  msg,
                  'outlining25@gmail.com',  # from
                  [request.user.email],  # to
                  fail_silently=False,
                  )

        messages.success(request, "Event is successfuly Booked !verify your mail")
        return render(request, 'event2.html')
    if request.user.is_authenticated:
        allevent4 = weddinghalls.objects.all()
        cont4 = {'il': allevent4}
        return render(request, 'event2.html',cont4)
    else:
        messages.success(request, "PLEASE LOGIN!")
    return redirect('/')


def event4(request):
    if request.method == 'POST':
        typeofevent = request.POST['tp']
        Name = request.POST['name']
        Date = str(request.POST['date'])
        starttime = str(request.POST['stime'])
        endtime = str(request.POST['etime'])
        venue = request.POST['venue']
        food = request.POST['food']
        selectdealer = request.POST['sdeal']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        if starttime == endtime:
            messages.success(request, "Both times should not be equal")
            return redirect('/event3')
        print(typeofevent, Name, Date, starttime, endtime, venue, food,selectdealer)
        book = event(type=typeofevent, cname=Name, cdate=Date, cstime=starttime, cetime=endtime, cvenue=venue,
                     cfood=food, sdealer=selectdealer,username=username)
        book.save()
        msg = "Your Event has been successfully booked"+"\n\n\n"+"EVENT DEATILS :"+"\n\n"+"Event Name :"+typeofevent+"\n"+"Name :"+Name+"\n"+"Date :"+Date+"\n"+"Your Dealer  Service Name :"+selectdealer+"\n"
        send_mail('Event Confirmation',  # subject
                  msg,
                  'outlining25@gmail.com',  # from
                  [request.user.email],  # to
                  fail_silently=False,
                  )

        messages.success(request, "Event is successfuly Booked !verify your mail")
        return render(request, 'event3.html')
    if request.user.is_authenticated:
        allevent4 = BirthdayParty.objects.all()
        cont4 = {'il': allevent4}
        return render(request, 'event3.html',cont4)
    else:
        messages.success(request, "PLEASE LOGIN!")
    return redirect('/')


def Caterings(request):
    if request.method == 'POST':
        stype=request.POST['dp']
        Servicename=request.POST['catername']
        Name1=request.POST['catername1']
        PPrice=request.POST['caterprice']
        Mobile=request.POST['caternum']
        Email=request.POST['cateremail']
        username = None
        if request.user.is_authenticated:
            username = request.user.username
        print(stype,Servicename,Name1,PPrice,Mobile,Email,username)
        cat = catering(type=stype,sname=Servicename,namemanu=Name1,pricemanu=PPrice,mobile=Mobile,emailmanu=Email,username=username)
        cat.save()
        messages.success(request,"Successfully added " )    
        return render(request,'caterings.html')
    if request.user.is_authenticated:
        return render(request,'caterings.html')
    else:
         messages.success(request, "PLEASE LOGIN!")
    return redirect('/dealerhome')

def MusicConcerts(request):
    if request.method == 'POST':
         stype1=request.POST['dp']
         cname=request.POST['bnames']
         Name=request.POST['namel']
         address=request.POST['address1']
         City=request.POST['citys']
         totprice=request.POST['price']
         Mobile=request.POST['nums']
         Email=request.POST['email2']
         if request.user.is_authenticated:
            username = request.user.username
         print(stype1,cname,Name,address,City,totprice,Mobile,Email,username)
         Music = Musicalconcertm(type1=stype1,conname=cname,name=Name,Address=address,City=City,Tprice=totprice,mobile=Mobile,email=Email,username=username)
         Music.save()
         messages.success(request,"Successfully added " )  
         return render(request,'Musicconcerts.html')
    if request.user.is_authenticated:
        return render(request,'Musicconcerts.html')
    else:
         messages.success(request, "PLEASE LOGIN!")
    return redirect('/dealerhome')

def weddinghall1(request):
    if request.method == 'POST':
         stype2=request.POST['dp']
         cname=request.POST['bname']
         Name=request.POST['name']
         address=request.POST['address']
         City=request.POST['city']
         totprice=request.POST['price']
         Mobile=request.POST['num']
         Email=request.POST['emails']
         if request.user.is_authenticated:
            username = request.user.username
         print(stype2,cname,Name,address,City,totprice,Mobile,Email,username)
         weddinghall1 = weddinghalls(type2=stype2,wname=cname,name=Name,Address=address,City=City,price=totprice,mobile=Mobile,email=Email,username=username)
         weddinghall1.save()
         messages.success(request,"Successfully added " )  
         return render(request,'weddinghall.html')
    if request.user.is_authenticated:
        return render(request,'weddinghall.html')
    else:
         messages.success(request, "PLEASE LOGIN!")
    return redirect('/dealerhome')


def Birthday(request):
    if request.method == 'POST':
        stype3 = request.POST['dp']
        venue = request.POST['birthdaynames']
        bname = request.POST['birthdayname']
        Address = request.POST['birthdayaddress1']
        City = request.POST['birthdaycitys']
        Price = request.POST['birthdayprices']
        Phone = request.POST['birthdaynums']
        email = request.POST['birthdayemails1']
        if request.user.is_authenticated:
            username = request.user.username
        print(stype3,venue,bname,Address,City,Price,Phone,email,username)
        party = BirthdayParty(type3=stype3,birthdayname=venue,birthdayame=bname,birthdayAddress=Address,birthdayCity=City,birthdayprice=Price,birthdaymobile=Phone,birthdayemail=email,username=username)
        party.save()
        messages.success(request,"Successfully added " )  
        return render(request,'Birthday.html')
    if request.user.is_authenticated:
        return render(request,'Birthday.html')
    else:
         messages.success(request, "PLEASE LOGIN!")
    return redirect('/dealerhome')


def contactform(request):
    if request.method == 'POST':
        name=request.POST['name']
        emailS=request.POST['email']
        stateS=request.POST['state']
        subjectS=request.POST['subject']
        if request.user.is_authenticated:
            username = request.user.username
        print(name,emailS,stateS,subjectS,username)
        contactform = contact1(Name=name,email=emailS,State=stateS,Subject=subjectS,username=username)
        contactform.save()
        msg = "Your Message has been reached to administrator! We will contact you with in 24 hours"
        if User.objects.filter(email=emailS).exists():
            send_mail('Query',  # subject
                  msg,
                  'outlining25@gmail.com',  # from
                   [emailS],  # to
                  fail_silently=False,
                  )

            messages.success(request, "Message sent." )
            return render(request,'contact.html')

    return render(request,'contact.html')
      

   

def dealercontacts1(request):
    if request.method == 'POST':
        dname=request.POST['dealername']
        demailS=request.POST['dealeremail']
        dstateS=request.POST['dealerstate']
        dsubjectS=request.POST['dealersubject']
        if request.user.is_authenticated:
            username = request.user.username
        print(dname,demailS,dstateS,dsubjectS,username)
        contactform = dcontact(DName=dname,Demail=demailS,DState=dstateS,DSubject=dsubjectS,username=username)
        contactform.save()
        messages.success(request, "Message sent." )

    return render(request,'dealercontact.html')


def loginout(request):
    logout(request)
    return redirect('/')

def loginout2(request):
    logout(request)
    return redirect('/dealerhome')





# forgot password

def fp1(request):
    c=None
    return render(request, 'forgotpass.html')


@csrf_exempt
def fp(request):
    email1=request.POST['email']
    if User.objects.filter(email=email1).exists():
        send_mail('Changing Password',  # subject
                  'http://127.0.0.1:8000/cp/',
                  'outlining25@gmail.com',  # from
                  [email1],  # to
                  fail_silently=False,
                  )
        messages.success(request,'Mail Successfully Sent')
        return render(request, 'forgotpass.html')
    messages.success(request, 'Email doesnot exist')
    return render(request, 'forgotpass.html')
    

def cp(request) :
    return render(request, 'cp.html')

@csrf_exempt
def cp1(request):
    username=request.POST['username']
    password=request.POST['Password']
    password1 = request.POST['re-enter Password']
    if password==password1:
        u=User.objects.get(username=username)
        u.set_password(password1)
        u.save()
        messages.success(request,"Password updated succcessfully")
        return redirect('/userlogin')
    else:
        return redirect('/cp1')





def fp2(request):
    c=None
    return render(request, 'forgotpass1.html')


@csrf_exempt
def fp3(request):
    email2=request.POST['email']
    if User.objects.filter(email=email2).exists():
        send_mail('Changing Password',  # subject
                  'http://127.0.0.1:8000/cp2/',
                  'outlining25@gmail.com',  # from
                  [email2],  # to
                  fail_silently=False,
                  )
        messages.success(request, 'Mail Successfully Sent')
        return render(request, 'forgotpass1.html')
    messages.success(request, 'Email doesnot exist')
    return render(request, 'forgotpass.html')

    

def cp2(request) :
    return render(request, 'cp1.html')


@csrf_exempt
def cp3(request):
    username=request.POST['username']
    password=request.POST['Password']
    password1 = request.POST['re-enter Password']
    if password==password1:
        u=User.objects.get(username=username)
        u.set_password(password1)
        u.save()
        messages.success(request,"Password updated succcessfully")
        return redirect('/dealerlogin')
    else:
        return redirect('/cp1')



