from django.contrib import admin
from django.urls import path, include
from . import views
from .views import home_page, ProfilePageView

app_name = 'players'
urlpatterns = [
    path('', views.home_page, name = 'home'),
    path('profile/<int:pk>/', ProfilePageView.as_view(), name = 'profile'),
    
]