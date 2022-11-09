from django.contrib import admin
from django.urls import path
from . import views
urlpatterns =[ path('',views.userlogin,name='login' ),
              path('userlogin/',views.userlogin,name='login' ),
              path('dash/',views.dash,name='dash' ),
              path('userregister/',views.userregister,name='register'),
              path('dealerlogin/',views.dealerlogin,name='login2' ),
              path('dealerregister/',views.dealerregister,name='register2'),
              path('dealerhome/',views.dealerhome,name="dealerhome"),
              path('home/',views.home,name="home"),
              path('history/',views.history,name='history'),
              path('faqs/',views.faqs,name="faqs"),
              path('contact/',views.contactform,name="contact"),
              path('contact/',views.contact,name="contact"),
              path('about/',views.about,name="about"),
              path('calender/',views.calender,name="calender"),
              path('userregisteruser',views.userregisteruser,name="registeruser"),
              path('userloginuser',views.userloginuser,name="loginuser"),
              path('dealerregisteruser',views.dealerregisteruser,name="registeruser2"),
              path('dealerloginuser',views.dealerloginuser,name="loginuser2"),
              path('event/',views.event1,name="event"),
              path('weddinghall/',views.weddinghall1,name="weddinghall"),
              path('cateringservice/',views.Catering,name="cateringservice"),
              path('Musicalconcert/',views.MusicConcerts,name="Musicalconcert"),
              

            
]
