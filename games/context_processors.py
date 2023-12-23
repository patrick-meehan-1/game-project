from .models import Game
from players.models import CustomUser

def menu_links(request):
    games = Game.objects.filter()
    return {'games': games}