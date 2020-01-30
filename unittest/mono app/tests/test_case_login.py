import unittest
import time
from driver import Driver
from screens.screen_login import LoginScreen
from credentials.credentials import Credentials

class LoginTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_login_screen(self):
        login = LoginScreen(self.driver)
        
        login.enter_url(Credentials.web_site_url)
        login.enter_username(Credentials.user_name)
        login.enter_psswrd(Credentials.password)
        login.save_psswrd()
        login.click_login()


    def tearDown(self):
        time.sleep(3)
        self.driver.instance.quit()
        print('Test Case finished')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
    