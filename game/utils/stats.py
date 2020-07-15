def update_stats(player):
    player.hp_max = round(player.power_crystals * 0.25)
    player.damage = round(player.power_crystals * 2.25)
    player.heal_cost = round(((player.hp_max - player.hp_current)*10)+100)