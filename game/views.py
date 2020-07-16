from django.shortcuts import render
from .utils import combat, stats
from .models import Player, Enemy

# Create your views here.
def game(request):

    e = Enemy.objects.all().order_by('power_crystals')

    try:
        p = Player.objects.get(user=request.user)
    except:
        p = Player(user=request.user)
        p.save()
    
    context = {
        "player": p,
        "enemies": e
        }
        
    if request.method == 'POST':
        #if 'gain_power_crystals_button' in request.POST:
        if request.POST.get('combat_button'):
            p = Player.objects.get(user=request.user)
            enemy_to_fight = Enemy.objects.get(name=request.POST.get('enemy_dropdown'))
            p, dmg_delt_player, dmg_delt_enemy, result = combat.fight(p, enemy_to_fight)

            context = {
                "player": p,
                "enemies": e,
                "result": result,
                "current_enemy": enemy_to_fight.name,
                "dmg_delt_player": dmg_delt_player,
                "dmg_delt_enemy": dmg_delt_enemy
                }

            if combat.check_alive(p):
                p.save()
            else:
                return render(request, 'game/ressurect.html', context)
        
        elif request.POST.get('heal_button_active'):
            p.gold -= p.heal_cost
            p.hp_current = p.hp_max
            p.save()


    stats.update_stats(p)
    p.save()
    return render(request, 'game/game.html', context)


def leaderboard(request):

    players_pc = Player.objects.all().order_by('-power_crystals')[:10]
    players_gold = Player.objects.all().order_by('-gold')[:10]

    context = {
        "players_pc": players_pc,
        "players_gold": players_gold
    }
    return render(request, 'game/leaderboard.html', context)


def ressurect(request):

    p = Player.objects.get(user=request.user)

    context = {
        "player": p
    }

    return render(request, 'game/ressurect.html', context)