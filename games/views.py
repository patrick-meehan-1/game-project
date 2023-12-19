from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .models import Game, Season
from players import models
from players.models import CustomUser
from django.contrib.auth import get_user_model


# Create your views here.

def game_details(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    seasons = game.seasons.all()

    return render(request, 'game.html', {'game': game, 'seasons': seasons})

class PlayerListView(ListView):
    model = CustomUser
    


def season_players(request, season_id):
    season = get_object_or_404(Season, id=season_id)
    players = season.players.all()
    return render(request, 'season.html', {'season': season, 'players': players})
