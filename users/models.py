from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, UserManager

'''

first_name (varchar 50) null = false
last_name (varchar 50) null = false
user_name (varchar 50) null = false
password (varchar 20) null = false
is_employee (boolean) null = true
picture
age
gender
occupation
address line 1
address line 2  (optional)
phone_number
description

'''
class User(AbstractBaseUser):
    email           = models.EmailField(unique=True)
    first_name      = models.CharField(max_length=50, null=False)
    last_name       = models.CharField(max_length=50, null=False)
    is_employee     = models.BooleanField(default=False)
    profile_picture = models.ImageField(max_length=50, null=True)
    age             = models.IntegerField(null=True)
    gender          = models.CharField(max_length=50, null=True)
    occupation      = models.CharField(max_length=50, null=True)
    address_line_1  = models.CharField(max_length=50, null=True)
    address_line_2  = models.CharField(max_length=50, null=True)
    phone_number    = models.CharField(max_length=50, null=False)
    description     = models.CharField(max_length=50, null=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()
class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'



