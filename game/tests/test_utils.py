from django.test import TestCase
from django.contrib.auth.models import User

from game.models import Player, Enemy
from game.utils import combat, logout, player_manager, stats


class TestGameUtils(TestCase):

    def setUp(self):
        self.test_user_one = User.objects.create(
            password='qwerty',
            username='djangodango',
            email='dandandjangodan@fjsdi.com'
        )
        self.test_player_one_dead = Player.objects.create(
            user=self.test_user_one,
            hp_current = 0
        )




    def test_combat_check_alive_function(self):
        self.assertFalse(combat.check_alive(self.test_player_one_dead))

