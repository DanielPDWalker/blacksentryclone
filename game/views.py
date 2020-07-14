from django.shortcuts import render
from .models import Player, Enemy

# Create your views here.
def game(request):

    e = Enemy.objects.all().order_by('power_crystals')

    try:
        p = Player.objects.get(user=request.user)
    except:
        p = Player(user=request.user)
        p.save()
    
        
    if request.method == 'POST':
        p = Player.objects.get(user=request.user)
        p.power_crystals += 1
        p.save()
    else:
        pass

    context = {
        "player": p,
        "enemies": e
        }

    return render(request, 'game/game.html', context)


def leaderboard(request):

    players = Player.objects.all().order_by('-power_crystals')[:10]

    context = {
        'players': players
    }
    return render(request, 'game/leaderboard.html', context)
