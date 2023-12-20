from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.
class CustomUser(AbstractUser):
    picture = models.ImageField(upload_to='profile_picture/', blank=True)
    picture_thumbnail = ImageSpecField(source='picture',
                                       processors=[ResizeToFill(200,200)],
                                       format='PNG',
                                       options={'quality':100})
    country = models.CharField(max_length=255, null=True, blank=True)
    points = models.PositiveBigIntegerField(null=True, blank=True)

class Profile(models.Model):
    player = models.OneToOneField(
        get_user_model(),
        null=True,
        on_delete=models.CASCADE,
    )
    bio = models.CharField(max_length=255)
    fun_fact = models.CharField(max_length=255)

    def __str__(self):
        return str(self.player)
    
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])