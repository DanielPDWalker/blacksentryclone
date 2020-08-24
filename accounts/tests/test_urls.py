from django.test import SimpleTestCase
from django.urls import reverse, resolve

from accounts.views import index, register


class TestAccountsUrls(SimpleTestCase):

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)