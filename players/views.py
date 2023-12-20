from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DetailView
from .models import CustomUser, Profile

# Create your views here.

def home_page(request):
    return render(request, 'home.html')

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'profile.html'
    context_object_name = 'profile'  # Set the context object name to 'profile'

    
    def get_object(self, queryset=None):
        # Use the user ID from the URL parameter to get the correct profile
        user_id = self.kwargs.get('pk')
        return get_object_or_404(Profile, player__id=user_id)