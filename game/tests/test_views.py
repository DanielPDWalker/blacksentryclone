from django.test import TestCase, Client
from django.urls import reverse


class TestGameViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_game_template(self):
        response = self.client.get(reverse('game'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/game.html')

    def test_leaderboard_template(self):
        response = self.client.get(reverse('leaderboard'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'game/leaderboard.html')
    