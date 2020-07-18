import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time



from local_test_settings import testpassword1, test_live_host



MAX_WAIT = 10

class GameplayTest(unittest.TestCase):

    username1 = 'edythe'
    email1 = 'edythe@gmail.com'
    password1 = testpassword1

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(test_live_host)

    def tearDown(self):
        self.browser.quit()


    def log_in(self):
        time.sleep(2)

        login = self.browser.find_element_by_id('login_button')
        login.send_keys(Keys.ENTER)

        time.sleep(2)

        username = self.browser.find_element_by_id('id_username')
        password = self.browser.find_element_by_id('id_password')
        login = self.browser.find_element_by_id('login_button')

        username.send_keys(self.username1)
        password.send_keys(self.password1)
        login.send_keys(Keys.ENTER)

        time.sleep(2)

    def combat(self, enemy):

        enemy_list = Select(browser.find_element_by_id('enemy_dropdown'))
        enemy_list.select_by_visible_text(enemy)
        # find fight button
        # send enter to fight button
        fight_button = browser.find_element_by_id('combat_button')
        fight_button.send_keys(Keys.ENTER)
        time.sleep(2)

    def test_fighting_rat(self):
        # Edythe returns to the site, and logs in.
        self.log_in()
        time.sleep(2)
        logged_in_text = self.browser.find_element_by_id('logged_in').text
        self.assertIn('edythe', logged_in_text)
        
        # She decides to try attacking a rat. 
        # (Anyone should be able to kill a rat).
        self.combat('Rat')
        success_text = self.browser.find_element_by_class_name('text-success').text
        self.assertIn('damaged and killed it!', success_text)

        
    def test_healing_after_ramage(self):
        # Edythe lusts for more rat blood. She attacks 5 more.
        for i in range(0, 5):
            self.combat('Rat')
        
        # She notices that by collecting enough power_crystals
        # her max hp has increased. She decides to heal.
        


        


    # Testing Heal

    # Fight another monster?

    # Fighting the highest level monster (dying)

    # Ressurect

    # Checking the leaderboard.

    # Changing her name.

if __name__ == "__main__":
    unittest.main()
