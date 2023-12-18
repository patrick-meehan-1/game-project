from django.contrib import admin
from django.urls import path, include
from . import views
from .views import GamePageView, SeasonPageView

app_name = 'games'
urlpatterns = [
    path('<int:pk>/', GamePageView.as_view(), name = 'game'),
    path('season/<int:pk>/', SeasonPageView.as_view(), name = 'season'),
    
]