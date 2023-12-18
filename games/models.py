from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='game_posters/')  
    num_seasons = models.PositiveIntegerField()

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse('game', args=[str(self.id)])

class Season(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='season_posters/', null=True)
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name='seasons'
    )
    players = models.ManyToManyField(
        get_user_model(),
        related_name='seasons',
    )

    def __str__(self):
        return f"{self.game.title} - {self.title}"
