from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    

    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return f'{self.email} {self.first_name} {self.last_name} {self.full_name}'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'