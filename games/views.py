from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .models import Game, Season
from players import models
from players.models import CustomUser
from django.contrib.auth import get_user_model


# Create your views here.

class GamePageView(DetailView):
    User = get_user_model()
    users = User.objects.all()
    model = Game
    template_name = 'game.html'

class PlayerListView(ListView):
    model = CustomUser
    


def season_players(request, season_id):
    season = get_object_or_404(Season, id=season_id)
    players = season.players.all()
    return render(request, 'season.html', {'season': season, 'players': players})
