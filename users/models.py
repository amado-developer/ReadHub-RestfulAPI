from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, UserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, profile_picture, age, gender, occupation
    , address_line_1, address_line2, phone_number, description, password, password2, balance):
        if password != password2:
            raise ValueError('passwords does not match')
        else:
            user = self.model(
                email=self.normalize_email(email),
                first_name = first_name,
                last_name = last_name,
                profile_picture = profile_picture,
                age = age, 
                gender = gender,
                occupation = occupation,
                address_line_1 = address_line2,
                address_line2 = address_line2,
                phone_number = phone_number,
                description = description,
                balance = balance,
            )

            user.set_password(password)
            # user.save()
            return user

class User(AbstractBaseUser):
    email           = models.EmailField(unique=True)
    first_name      = models.CharField(max_length=50, null=False)
    last_name       = models.CharField(max_length=50, null=False)
    profile_picture = models.ImageField(max_length=None, null=True)
    age             = models.IntegerField(null=True)
    gender          = models.CharField(max_length=50, null=True)
    occupation      = models.CharField(max_length=50, null=True)
    address_line_1  = models.CharField(max_length=50, null=True)
    address_line_2  = models.CharField(max_length=50, null=True)
    phone_number    = models.CharField(max_length=50, null=False)
    description     = models.CharField(max_length=50, null=True)
    balance         = models.FloatField(null=True, default=0.0)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'

