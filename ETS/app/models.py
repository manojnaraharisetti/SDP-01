from django.db import models
from unittest.util import _MAX_LENGTH
import datetime
from django.core.exceptions import ValidationError

class event(models.Model):
    username=models.CharField(max_length=200)
    type=models.CharField(max_length=200)
    cname=models.CharField(max_length=200)
    cdate=models.CharField(max_length=20)
    cstime=models.CharField(max_length=20)
    cetime=models.CharField(max_length=20)
    cvenue=models.CharField(max_length=200)
    cfood=models.CharField(max_length=10)

    def __str__(self):
        return ' Name : '+self.cname+' - Date : '+self.cdate


class catering(models.Model):
    username=models.CharField(max_length=200)
    sname=models.CharField(max_length=200)
    namemanu=models.CharField(max_length=200)
    pricemanu=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    emailmanu=models.CharField(max_length=200)
    

    def __str__(self):
        return ' Name : '+self.namemanu+' - Event : '+self.sname

class Musicalconcertm(models.Model):
    username=models.CharField(max_length=200)
    conname=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    pcode=models.CharField(max_length=200)
    Tprice=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10)
    email=models.CharField(max_length=200)

    def __str__(self):
        return ' Name : '+self.name+' - Event : '+self.conname

class weddinghalls(models.Model):
    username=models.CharField(max_length=200)
    wname=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    pcode=models.CharField(max_length=200)
    price=models.CharField(max_length=200)
    mobile=models.CharField(max_length=10)
    email=models.CharField(max_length=200)

    def __str__(self):
        return ' Name : '+self.name+' - Event : '+self.wname




    
