from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# from django.contrib.auth.models import 
# Create your models here.

class UserModel(AbstractBaseUser):
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.GeneratedField(
        expression = models.F('first_name') + models.F('last_name'),
        output_field = models.CharField(max_length=200), 
        db_persist = True
    )

