from django.contrib import admin

# Register your models here.


# from socket import SOL_NETROM
import unittest.util
from django.db import models

# Create your models here.
from .models import event,catering,Musicalconcertm,weddinghalls,BirthdayParty,contact1,dcontact
admin.site.register(event)
admin.site.register(catering)
admin.site.register(Musicalconcertm)
admin.site.register(weddinghalls)
admin.site.register(BirthdayParty)
admin.site.register(contact1)
admin.site.register(dcontact)