from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from MatchBookBack.abstracts.base_models import BaseModel

class User(AbstractBaseUser, BaseModel):
    REQUIRED_FIELDS = ['first_name', 'last_name', 'password']
    USERNAME_FIELD = 'email'

    first_name = models.CharField(max_length=255, verbose_name='Nome')
    last_name = models.CharField(max_length=255, verbose_name='Sobrenome')
    email = models.EmailField(max_length=255, unique=True, verbose_name='E-mail')
    password = models.CharField(max_length=255, verbose_name='Senha')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Latitude')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Longitude')