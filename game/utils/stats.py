def update_stats(player):
    """Updates player stats in the database based on power crystals."""
    player.hp_max = round(player.power_crystals * 0.25)
    if player.hp_current > player.hp_max:
        player.hp_current = player.hp_max
    player.damage = round(player.power_crystals * 2.25)
    player.heal_cost = round(((player.hp_max - player.hp_current))+10)
