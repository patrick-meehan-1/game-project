from .models import Game

def menu_links(request):
    games = Game.objects.filter()
    return {'games': games}