import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

from .local_test_settings import testpassword1, test_live_host


class MovingAroundSiteTest(unittest.TestCase):

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
        # Edythe has heard of this hip new game called "Battle Abyss".
        # She decides to go visit.
        self.browser.get(test_live_host)
        # She logs in
        self.log_in()

        # Edythe notices that her name appears in the logged in text.
        self.assertIn('edythe', self.browser.find_element_by_id('logged_in').text)

        # Edythe goes to the leaderboard to check out the top 10 players.
        self.browser.find_element_by_id('navbar_leaderboard').click()
        self.assertIn('Top 10', self.browser.find_element_by_tag_name('h4').text)

        # She then goes to see whats on the "Change Name" page.
        self.browser.find_element_by_id('navbar_namechanger').click()
        self.assertIn('Do you wish to change your', self.browser.find_element_by_id('main_text').text)

        # Edythe goes back to main game page.
        self.browser.find_element_by_id('navbar_game').click()
        self.assertIn('Choose an enemy', self.browser.find_element_by_id('enemy_dropdown_label').text)

        # After all her tiring browsing, Edythe decides to log out.
        self.browser.find_element_by_id('navbar_logout').click()
        self.assertIn('About the game', self.browser.find_element_by_tag_name('h3').text)


        
        
