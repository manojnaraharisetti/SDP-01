from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=200)
    dob=models.CharField(max_length=50)
    companyname = models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(  max_length=16)
