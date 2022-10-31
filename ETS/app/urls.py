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
             path('login',views.login,name='login' ),
            path('calender',views.calender,name="calender") ,
            path('registeruser',views.registeruser,name="registeruser"),
            path('loginuser',views.loginuser,name="loginuser"),
]
