import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


from local_test_settings import testpassword1, test_live_host



MAX_WAIT = 10

class NewVisitorTest(unittest.TestCase):

    username1 = 'edythe'
    email1 = 'edythe@gmail.com'
    password1 = testpassword1

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(test_live_host)

    def tearDown(self):
        self.browser.quit()

    def sign_up(self):
        #Find better way to wait untill page loads?
        time.sleep(2)

        register = self.browser.find_element_by_id('register_button')
        register.send_keys(Keys.ENTER)

        time.sleep(2)

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
        time.sleep(2)

        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        login = self.browser.find_element_by_id('login_button')

        username.send_keys(self.username1)
        password.send_keys(self.password1)
        login.send_keys(Keys.ENTER)

    def test_signup(self):
        # Edythe has heard of this hip new game called "I DONT KNOW HOW TO NAME THINGS".
        # She decides to sign up.

        self.sign_up()

        # She immediately logs in.
        self.log_in()
        time.sleep(2)
        self.assertIn('edythe', self.browser.find_element_by_id('logged_in'))


if __name__ == "__main__":
    unittest.main()
