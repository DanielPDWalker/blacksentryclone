from ..models import Player

import random
import os


def get_random_username():
    base_dir = os.path.dirname(__file__)
    adjectives = []
    nouns = []

    with open(os.path.join(base_dir, 'names/adjectives.txt'), 'r') as a_file:
        for name in a_file:
             adjectives.append(name.strip())

    with open (os.path.join(base_dir, 'names/nouns.txt'), 'r') as n_file:
        for name in n_file:
            nouns.append(name.strip())

    username = random.choice(adjectives).title() + random.choice(nouns).title() + str(random.randrange(1000))

    if username in Player.objects.filter(name=username):
        get_random_username()
    else:
        return username

def init_player(user_obj):
    username = get_random_username()

    p = Player(user=user_obj)
    p.name = username

    return p


def change_name(player_obj):
    username = get_random_username()

    player_obj.name = username
    player_obj.save()