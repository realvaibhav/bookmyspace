from django.db import models

# Create your models here.
class users_signup(models.Model):
    name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=13, default='+91')
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=32)
    confirm_password = models.CharField(max_length=32)
    