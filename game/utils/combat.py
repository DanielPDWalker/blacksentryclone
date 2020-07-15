import random

def check_alive(player):
    if player.hp_current > 0:
        return True
    else:
        return False


def fight(player, enemy):
    """
    This will cause a round of combat between the user and their selected enemy. 
    It will return the changes to the player object and an result
    Boolean. True (win) or False (loss).
    """

    # Replace the 8 with rng 8-10
    dmg_roll_player = player.damage * 8
    
    if enemy.hp_max <= dmg_roll_player:
        player.power_crystals += enemy.power_crystals
        player.gold += enemy.gold
        dmg_roll_enemy = 0
        result = True
    else:
        result = False
        # Again we can add some rng on the dmg here.
        dmg_roll_enemy = enemy.damage * 2
        player.hp_current -= dmg_roll_enemy

    return [player, dmg_roll_player, dmg_roll_enemy, result]