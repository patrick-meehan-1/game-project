from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    country = models.CharField(max_length=255, null=True, blank=True)
    pin = models.PositiveIntegerField(null=True, blank=True)