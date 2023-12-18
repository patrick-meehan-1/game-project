from django.urls import path, include
from . import views
from .views import GamePageView, season_players

app_name = 'games'
urlpatterns = [
    path('<int:pk>/', GamePageView.as_view(), name = 'game'),
    path('season/<int:season_id>/', views.season_players, name = 'season'),
    
]