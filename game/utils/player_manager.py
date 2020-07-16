from ..models import Player


## Replace all this username stuff with "pip install random-username"
import random
import csv


f_names = list(csv.reader('first_names.csv'))
s_names = list(csv.reader('second_names.csv'))


def init_player(player_obj):
    
    random_number = random.randrange(0, len(f_names))
    name_picked = f_names[random_number] + ' '

    random_number = random.randrange(0, len(s_names))
    name_picked  += s_names[random_number]
    if name_picked in Player.objects.filter(name=name_picked):
        init_player(player_obj)
    else:
        p = Player(player_obj)
        p.name = name_picked
        p.save()



def change_name(player_obj):
    random_number = random.randrange(0, len(f_names))
    name_picked = str(f_names[random_number]) + ' '

    random_number = random.randrange(0, len(s_names))
    name_picked  += str(s_names[random_number])

    if name_picked in Player.objects.filter(name=name_picked):
        change_name(player_obj)
    else:
        player_obj.name = name_picked
        player_obj.save()