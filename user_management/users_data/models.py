# Create your models here.
from django.db import models
import datetime,sys

class Users(models.Model):
    first_name = models.CharField(max_length=40,help_text="first name of the user",unique=True)
    middle_name = models.CharField(max_length=40,help_text="middle name of the user",blank=True)
    last_name = models.CharField(max_length=40,help_text="last name of the user")
    email=models.CharField(max_length=40,help_text="email of the user")
    phone_number = models.IntegerField(max_length=20)
    created_date_time=models.DateTimeField(auto_now_add=True)
    modified_date_time=models.DateTimeField(auto_now=True)

