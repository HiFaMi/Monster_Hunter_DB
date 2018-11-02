from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models

# Create your models here.


class UserManager(DjangoUserManager):
    def create_django_user(self, *args, **kwargs):
        user = User.objects.create_user(
            username=kwargs.get('username'),
            email=kwargs.get('email'),
            password=kwargs.get('password'),
            first_name=kwargs.get('first_name', ''),
            phone_number=kwargs.get('phone_number', ''),
        )
        return user


class User(AbstractUser):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    create_date = models.DateField(auto_now_add=True)
