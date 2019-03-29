from django.db import models
from django.core import validators

# Create your models here.

class EmpFresher(models.Model):
     name=models.CharField(max_length=20)
     Email_ID = models.EmailField()
     phone_number = models.CharField(max_length=12)
     location=models.CharField(max_length=40)

class EmpProfessional(models.Model):
    name=models.CharField(max_length=20)
    Email_ID =models.EmailField()
    phone_number = models.CharField(max_length=12)
    location=models.CharField(max_length=40)



