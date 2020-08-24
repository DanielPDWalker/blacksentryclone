from django.test import TestCase, Client
from django.urls import reverse


class TestAccountsViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_index_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/index.html')
    
    def test_register_template(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')