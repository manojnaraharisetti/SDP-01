from django.urls import path
from . import views
urlpatterns =[path('',views.dash,name='dash' ),
              path('register',views.register,name='register'),
              path('home',views.home,name="home"),
              path('history',views.history,name='history'),
path('faqs',views.faqs,name="faqs"),
path('event',views.event,name="event"),
path('contact',views.contact,name="contact"),
path('about',views.about,name="about"),
path('login2',views.login2,name='login2' ),
path('login',views.login,name='login2' ),
path('register2',views.register2,name='register2'),
path('calender',views.calender,name="calender")
]
