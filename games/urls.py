from django.urls import path, include
from . import views
from .views import game_details, season_players

app_name = 'games'
urlpatterns = [
    path('leaderboard/', views.leaderboard, name = 'leaderboard'),
    path('<int:game_id>/', views.game_details, name = 'game'),
    path('season/<int:season_id>/', views.season_players, name = 'season'),
    
]