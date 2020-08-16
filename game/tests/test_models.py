from django.test import TestCase
from django.contrib.auth.models import User

from game.models import Player, Enemy


class TestGameModels(TestCase):

    def setUp(self):
        self.test_user = User.objects.create(
            password='qwerty',
            username='djangodango',
            email='dandandjangodan@fjsdi.com'
        )

        self.test_player = Player.objects.create(
            user=self.test_user
        )

        self.test_enemy = Enemy.objects.create(
            name='Ratman'
        )

    def test_random_username_generated_for_player_on_creation(self):
        self.assertTrue(self.test_player.name != None)
    
    def test_name_return_for_test_player(self):
        self.assertEquals(self.test_player.__str__(), self.test_player.user.username)

    def test_name_return_for_test_enemy(self):
        self.assertEquals(self.test_enemy.__str__(), self.test_enemy.name)
    