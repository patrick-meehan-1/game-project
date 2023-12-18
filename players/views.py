from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DetailView
from .models import CustomUser, Profile

# Create your views here.

def home_page(request):
    return render(request, 'base.html')

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'profile.html'