from ..models import Player

import random
import os


def get_random_username():
    base_dir = os.path.dirname(__file__)
    first_word = []
    noun = []

    with open(os.path.join(base_dir, 'names/first_word.txt'), 'r') as a_file:
        for name in a_file:
             first_word.append(name.strip())

    with open (os.path.join(base_dir, 'names/noun.txt'), 'r') as n_file:
        for name in n_file:
            noun.append(name.strip())

    username = random.choice(first_word).title() + random.choice(noun).title() + str(random.randrange(1000))

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