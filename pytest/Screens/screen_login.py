import time
from appium.webdriver.common.mobileby import MobileBy


class LoginScreenAndroid:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver

        pckgnm = "com.icertainty.forms:id/"

        #LOGIN SCREEN:
        self.login_screen_logo = (MobileBy.ID, pckgnm+"LoginFragment_Logo")
        self.login_screen_url = (MobileBy.ID, pckgnm+"LoginFragment_Url")
        self.login_screen_usrnm = (MobileBy.ID, pckgnm+"LoginFragment_UserName")
        self.login_screen_psswrd = (MobileBy.ID, pckgnm+"LoginFragment_Password")
        self.login_screen_save_psswrd = (MobileBy.ID, pckgnm+"LoginFragment_KeepPass")
        self.login_button = (MobileBy.ID, pckgnm+"LoginFragment_LoginBtn")
        self.app_version = (MobileBy.ID, pckgnm+"LoginFragment_VersionNumber")

    def enter_credentials(self, url, usrnm, psswrd):
        self.app.wait_element(self.login_screen_url).send_keys(url)
        self.app.wait_element(self.login_screen_usrnm).send_keys(usrnm)
        self.app.wait_element(self.login_screen_psswrd).send_keys(psswrd)
        print(f'- Credentials: {usrnm} and /password/ are introduced for {url}')

    def save_psswrd(self):
        selected = self.app.wait_element(self.login_screen_save_psswrd).is_selected()

        if selected:
            print('Password already saved')
        else:
            self.app.wait_element(self.login_screen_save_psswrd).click()
            print('- Saving the Password')

    def click_login(self):
        self.app.wait_element(self.login_button).click()
        print('- Trying to log in...')
