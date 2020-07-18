from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time


from bsc.local_settings import testpassword1



MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    username1 = 'edythe'
    email1 = 'edythe@gmail.com'
    password1 = testpassword1

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def sign_up(self):
        #Find better way to wait untill page loads?
        time.sleep(2)

        register = self.browser.find_element_by_id('register_button')
        register.send_keys(Keys.ENTER)

        #Find better way to wait untill page loads?
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
        #Find better way to wait untill page loads?
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
        self.browser.get(self.live_server_url)

        self.sign_up()

        self.log_in()

        time.sleep(3)

        

        
    



        self.fail('Finish the signup test!')
