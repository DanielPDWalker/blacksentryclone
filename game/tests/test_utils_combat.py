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
        self.test_player_one = Player.objects.create(
            user=self.test_user_one,
            hp_current = 0
        )

        self.test_user_two = User.objects.create(
            password='qwerty1',
            username='djangodango1',
            email='dandandjangodan1@fjsdi.com'
        )
        self.test_player_two = Player.objects.create(
            user=self.test_user_two
        )


        self.test_enemy_rat = Enemy.objects.create(
            name='Rat',
            power_crystals=1,
            hp_current=1,
            hp_max=1,
            gold=1,
            damage=1
        )

        self.test_enemy_swings_back = Enemy.objects.create(
            name='Tank',
            power_crystals=1,
            hp_current=10000,
            hp_max=10000,
            gold=1,
            damage=1
        )

        self.test_enemy_death = Enemy.objects.create(
            name='Death',
            power_crystals=10000000,
            hp_current=10000000,
            hp_max=10000000,
            gold=10000000,
            damage=10000000
        )

    def test_combat_check_alive_function_success(self):
        self.assertTrue(combat.check_alive(self.test_player_two))

    def test_combat_check_alive_function_fail(self):
        self.assertFalse(combat.check_alive(self.test_player_one))

    def test_combat_fight_function_success(self):
        # Check winning a fight vs Rat - (result)
        self.assertEquals(combat.fight(self.test_player_two, self.test_enemy_rat )[3], True)
        # Check winning a fight vs Rat - (dmg_roll_enemy)
        self.assertEquals(combat.fight(self.test_player_two, self.test_enemy_rat )[2], 0)
        # Check winning a fight vs Rat - (looted_gold)
        self.assertNotEquals(combat.fight(self.test_player_two, self.test_enemy_rat )[4], 0)
        # Check winning a fight vs Rat - (looted_power_crystals)
        self.assertNotEquals(combat.fight(self.test_player_two, self.test_enemy_rat )[5], 0)

    def test_combat_fight_function_fail_no_death(self):
        # Check taking a hit from the "Tank" enemy
        # Check result of combat is False
        self.assertEquals(combat.fight(self.test_player_two, self.test_enemy_swings_back )[3], False)
        # Check that the enemy has done damage back
        self.assertNotEquals(combat.fight(self.test_player_two, self.test_enemy_swings_back )[2], 0)      
        # looted_gold should be 0 for a loss
        self.assertEquals(combat.fight(self.test_player_two, self.test_enemy_swings_back )[4], 0)
        # looted_power_crystals should be 0 for a loss
        self.assertEquals(combat.fight(self.test_player_two, self.test_enemy_swings_back )[5], 0)  
    
    def test_combat_fight_function_fail_with_death(self):
        # Check dying fighting "Death"
        pass
