from django.urls import path
from . import views
urlpatterns =[path('',views.login,name='login' ),
              path('register',views.register,name='register'),
              path('home',views.home,name="home"),
              path('history',views.history,name='history'),
path('faqs',views.faqs,name="faqs"),
path('event',views.event,name="event"),
path('contact',views.contact,name="contact"),
path('about',views.about,name="about")
]
