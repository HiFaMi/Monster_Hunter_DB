from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models

# Create your models here.


class UserManager(DjangoUserManager):
    def create_django_user(self, *args, **kwargs):
        user = User.objects.create_user(
            username=kwargs.get('username'),
            email=kwargs.get('email'),
            password=kwargs.get('password'),
        )
        return user


class User(AbstractUser):
    AUTH_CHOICE = (
        ('A', 'Local Auth'),
        ('K', 'Kakao'),
        ('N', 'Naver'),
    )

    MODEL_CHECK = (
        ('n', 'Not'),
        ('y', 'Yes'),
    )

    username = models.CharField(max_length=200, unique=True, verbose_name='ID')
    auth = models.CharField(max_length=1, choices=AUTH_CHOICE, default='A')
    email = models.CharField(max_length=50)
    email_check = models.CharField(max_length=1, default='n')
    create_at = models.DateField(auto_now_add=True)

