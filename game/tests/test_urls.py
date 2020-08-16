from django.test import SimpleTestCase
from django.urls import reverse, resolve

from game.views import game, leaderboard, resurrect, namechanger


class TestGameUrls(SimpleTestCase):

    def test_game_url_resolves(self):
        url = reverse('game')
        self.assertEquals(resolve(url).func, game)
    
    def test_leaderboard_url_resolves(self):
        url = reverse('leaderboard')
        self.assertEquals(resolve(url).func, leaderboard)

    def test_resurrect_url_resolves(self):
        url = reverse('resurrect')
        self.assertEquals(resolve(url).func, resurrect)

    def test_namechanger_url_resolves(self):
        url = reverse('namechanger')
        self.assertEquals(resolve(url).func, namechanger)    
