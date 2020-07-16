from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import combat, stats, player_manager
from .models import Player, Enemy

# Create your views here.
def game(request):

    e = Enemy.objects.all().order_by('power_crystals')

    try:
        p = Player.objects.get(user=request.user)
    except:
        player_manager.init_player(user=request.user)

    if not combat.check_alive(p):
        return redirect(resurrect)

    context = {
        "player": p,
        "enemies": e
        }
        
    if not combat.check_alive(p):
        return render(request, 'game/resurrect.html', context)

    if request.method == 'POST':
        #if 'gain_power_crystals_button' in request.POST:
        if request.POST.get('combat_button'):
            p = Player.objects.get(user=request.user)
            enemy_to_fight = Enemy.objects.get(name=request.POST.get('enemy_dropdown'))
            p, dmg_delt_player, dmg_delt_enemy, result = combat.fight(p, enemy_to_fight)
            player_manager.change_name(p)

            context = {
                "player": p,
                "enemies": e,
                "result": result,
                "current_enemy": enemy_to_fight.name,
                "dmg_delt_player": dmg_delt_player,
                "dmg_delt_enemy": dmg_delt_enemy
                }
            
            p.save()
            if not combat.check_alive(p):
                return redirect(resurrect)
                
        
        elif request.POST.get('heal_button_active'):
            p.gold -= p.heal_cost
            p.hp_current = p.hp_max


    stats.update_stats(p)
    p.save()
    return render(request, 'game/game.html', context)


def leaderboard(request):

    players_pc = Player.objects.filter(is_banned=False).order_by('-power_crystals')[:10]
    players_gold = Player.objects.filter(is_banned=False).order_by('-gold')[:10]

    context = {
        "players_pc": players_pc,
        "players_gold": players_gold
    }
    return render(request, 'game/leaderboard.html', context)


def resurrect(request):
    p = Player.objects.get(user=request.user)
    e = Enemy.objects.all().order_by('power_crystals')

    if request.POST.get('resurrect_button'):
        p.gold -= p.gold
        p.hp_current = p.hp_max
        p.save()

        context = {
        "player": p,
        "enemies": e
        }

        return redirect(game)
    context = {
        "player": p,
        "enemies": e
        }
        
    return render(request, 'game/resurrect.html', context)