
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.conf import settings
# Create your models here.

class CustomUser(AbstractUser):
    idGame = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=11,null=True, blank=True)
    


