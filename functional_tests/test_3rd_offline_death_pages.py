import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
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

    def fight_better_known_as_die_to_death_the_entity_not_the_status(self):

        enemy_list = Select(self.browser.find_element_by_id('enemy_dropdown_list'))

        # find fight button
        enemy_list.select_by_visible_text('Death')
        # send enter to fight button
        fight_button = self.browser.find_element_by_name('combat_button')

        fight_button.send_keys(Keys.ENTER)
        # Allow the rest of the template to update/reload.
        time.sleep(0.5)  

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

    def test_death_and_moving_around_site(self):
        # Edythe go back to Battle Abyss.
        self.browser.get(test_live_host)
        # She logs in
        self.log_in()

        # Edythe notices that her name appears in the logged in text.
        logged_in_text = self.browser.find_element_by_id('logged_in').text
        self.assertIn('edythe', logged_in_text)

        # Edythe, throwing all caution to the wind, takes a swing at death itself.

        self.fight_better_known_as_die_to_death_the_entity_not_the_status()

        # Edythe suprising sees she has died, and is presented with a
        # resurrect button.
        try:
            element = self.browser.find_element_by_name('resurrect_button')
        except NoSuchElementException:
            self.fail('The resurrect button isnt being shown.')

        # Wishing to spend some time counted among the dead, Edythe
        # checks out the leaderboard before returning to life.
        self.browser.find_element_by_id('navbar_leaderboard').click()
        self.assertIn('Top 10', self.browser.find_element_by_tag_name('h4').text)

        # She then goes to see whats on the "Change Name" page.
        self.browser.find_element_by_id('navbar_namechanger').click()
        try:
            element = self.browser.find_element_by_id('resurrect_redirect')
        except NoSuchElementException:
            self.fail('The resurrect redirect isnt being shown.')
        
        # Finally Edythe goes back to the main game screen.
        self.browser.find_element_by_id('navbar_game').click()
        try:
            # She clicks the resurrect button.
            self.browser.find_element_by_id('resurrect_button').send_keys(Keys.ENTER)
        except NoSuchElementException:
            self.fail('The resurrect button isnt being shown.')
        
        # She notices that the main game screen has come back.
        self.assertIn('Choose an enemy', self.browser.find_element_by_id('enemy_dropdown_label').text)

        # Edythe decides to call it a day, and logs out.
        self.browser.find_element_by_id('navbar_logout').click()
        self.assertIn('About the game', self.browser.find_element_by_tag_name('h3').text)
