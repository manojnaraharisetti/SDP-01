from django.db import models

# Create your models here.
class Registerpg(models.Model):
    fn=models.CharField(max_length=200)
    ln=models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    uname = models.CharField(max_length=200)
    password=models.CharField(max_length=16)
