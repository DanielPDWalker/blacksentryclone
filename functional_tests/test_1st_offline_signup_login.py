import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from .local_test_settings import testpassword1, test_live_host


class NewVisitorTest(unittest.TestCase):

    username1 = 'edythe'
    email1 = 'edythe@gmail.com'
    password1 = testpassword1

    def setUp(self):
        self.browser = webdriver.Firefox('functional_tests')
        self.browser.implicitly_wait(10)
           
    def tearDown(self):
        self.browser.quit()

    def sign_up(self):
        register = self.browser.find_element_by_id('register_button')
        register.send_keys(Keys.ENTER)

        username = self.browser.find_element_by_id('id_username')
        email = self.browser.find_element_by_id('id_email')
        password = self.browser.find_element_by_id('id_password1')
        password_confirm = self.browser.find_element_by_id('id_password2')
        register = self.browser.find_element_by_id('register_button')

        username.send_keys(self.username1)
        email.send_keys(self.email1)
        password.send_keys(self.password1)
        password_confirm.send_keys(self.password1)
        register.send_keys(Keys.ENTER)        

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

    def test_signup_and_login(self):
        # Edythe has heard of this hip new game called "Battle Abyss".
        # She decides to go visit.
        self.browser.get(test_live_host)
        # logs in
        self.log_in()

        # Edythe notices that her name appears in the logged in text.
        self.assertIn('edythe', self.browser.find_element_by_id('logged_in').text)

