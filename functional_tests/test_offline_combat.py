import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from .local_test_settings import testpassword1, test_live_host


class BasicCombatAndHealTest(unittest.TestCase):

    username1 = 'edythe'
    email1 = 'edythe@gmail.com'
    password1 = testpassword1

    def setUp(self):
        self.browser = webdriver.Firefox('functional_tests')
        self.browser.implicitly_wait(10)     
    
    def tearDown(self):
        self.browser.quit()

    def fight_rat(self, enemy, rounds=1):
        counter = 0
        while counter < rounds:
            enemy_list = Select(self.browser.find_element_by_id('enemy_dropdown_list'))

            enemy_list.select_by_visible_text(enemy)
            # find fight button
            # send enter to fight button
            fight_button = self.browser.find_element_by_name('combat_button')

            fight_button.send_keys(Keys.ENTER)
            self.assertIn('damage and killed it!', self.browser.find_element_by_class_name('text-success').text)

            counter += 1
        # Allow the rest of the template to update/reload after the combat spam.
        time.sleep(0.5)   

    def log_in(self):
        #Find better way to wait untill page loads?
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

    def test_combat_and_healing(self):
        # Edythe decides to got back to battleabyss.com and kill some rats.
        self.browser.get(test_live_host)
        # She logs in
        self.log_in()
        # Edythe notices that her name appears in the logged in text.
        logged_in_text = self.browser.find_element_by_id('logged_in').text
        self.assertIn('edythe', logged_in_text)
        # She decides to fight rats 25 times!
        self.fight_rat('Rat', rounds=25)

        # Edythe clicks on the heal button, as she has more max hp now!
        self.browser.find_element_by_name('heal_button_active').click()

        try:
            element = self.browser.find_element_by_name('heal_button_disabled')
        except NoSuchElementException:
            self.fail('Heal button was not clicked, the disabled heal button isnt showing.')

        

