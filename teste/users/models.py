from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    nasc = models.DateField(null=True)
