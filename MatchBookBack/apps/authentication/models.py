from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager

from MatchBookBack.abstracts.base_models import BaseModel

class UserProfileImage(BaseModel):

    url = models.CharField(max_length=255, null=True, blank=True)
    delete_hash = models.CharField(max_length=255, null=True, blank=True)

    class Meta():
        app_label = 'authentication'

class User(AbstractBaseUser, BaseModel):
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
    USERNAME_FIELD = 'email'

    first_name = models.CharField(max_length=255, verbose_name='Nome')
    last_name = models.CharField(max_length=255, verbose_name='Sobrenome')
    email = models.EmailField(max_length=255, unique=True, verbose_name='E-mail')
    password = models.CharField(max_length=255, verbose_name='Senha')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Latitude')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Longitude')
    profile_image = models.ForeignKey(UserProfileImage, on_delete=models.CASCADE, null=True, blank=True)

    objects = UserManager()

    class Meta():
        app_label = 'authentication'