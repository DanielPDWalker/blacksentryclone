import random


def check_alive(player):
    """ Return true or false on if player is alive """
    if player.hp_current > 0:
        return True
    else:
        return False


def fight(player, enemy):
    """
    This starts a round of combat between the user and their selected enemy.

    It returns a list of information relating to combat, to be used in the
    view function to display it, if required.
    """

    # Random player damage based on 80-100% of player damage stat.
    dmg_range_roll = random.randrange(80, 101) / 100
    dmg_roll_player = round(player.damage * dmg_range_roll)

    looted_power_crystals = 0
    looted_gold = 0

    if enemy.hp_max <= dmg_roll_player:
        # Randomly generated loot values, added to player object.
        resources_range_roll = random.randrange(75, 101) / 100
        looted_power_crystals = round(
            enemy.power_crystals * resources_range_roll)
        player.power_crystals += looted_power_crystals

        resources_range_roll = random.randrange(75, 101) / 100
        looted_gold = round(enemy.gold * resources_range_roll)
        player.gold += looted_gold

        dmg_roll_enemy = 0
        result = True
    else:
        result = False
        # Random enemy damage, based on 80-100% of their damage stat.
        dmg_range_roll = random.randrange(80, 101) / 100
        dmg_roll_enemy = round(enemy.damage * dmg_range_roll)
        player.hp_current -= dmg_roll_enemy

    return [player, dmg_roll_player, dmg_roll_enemy, result, looted_gold, looted_power_crystals]
