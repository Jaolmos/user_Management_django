from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('f', 'female'),
    )

    username = models.CharField('Username', max_length=20, unique=True)
    email = models.EmailField()
    first_name = models.CharField('First name', max_length=30, blank=True)
    last_name = models.CharField('First name', max_length=30, blank=True)
    gender = models.CharField('Gender', max_length=1, choices=GENDER_CHOICES, blank=True)

    USERNAME_FIELD = 'username'

    object = UserManager()

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


