import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

from .local_test_settings import testpassword1, test_live_host


class DeathPagesTest(unittest.TestCase):

    username1 = 'edythe'
    email1 = 'edythe@gmail.com'
    password1 = testpassword1

    def setUp(self):
        self.browser = webdriver.Firefox('functional_tests')
        self.browser.implicitly_wait(10)
    
    def tearDown(self):
        self.browser.quit()

    def log_in(self):
        try:
            self.browser.find_element_by_id('home_button').send_keys(Keys.ENTER)
        except:
            pass

        self.browser.find_element_by_id('login_button').send_keys(Keys.ENTER)

        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        login = self.browser.find_element_by_id('login_button')

        username.send_keys(self.username1)
        password.send_keys(self.password1)
        login.send_keys(Keys.ENTER)

    def test_moving_around_site(self):
        # Edythe go back to Battle Abyss.
        self.browser.get(test_live_host)
        # She logs in
        self.log_in()

        # Edythe, throwing all caution to the wind, takes a swing at death itself.
