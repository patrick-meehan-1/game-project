from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView, ListView
from .models import Game, Season
from players import models
from players.models import CustomUser

# Create your views here.

class GamePageView(DetailView):
    model = Game
    template_name = 'game.html'

class SeasonPageView(DetailView):
    model = Season
    template_name = 'season.html'

class PlayerListView(ListView):
    model = CustomUser
    