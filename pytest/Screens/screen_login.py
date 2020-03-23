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
        url_name = self.app.wait_element(self.login_screen_url)
        url_name.clear()
        url_name.send_keys(url)
        user_name = self.app.wait_element(self.login_screen_usrnm)
        user_name.clear()
        user_name.send_keys(usrnm)
        pass_word = self.app.wait_element(self.login_screen_psswrd)
        pass_word.clear()
        pass_word.send_keys(psswrd)
        print(f'- Typing in credentials: {usrnm} and /password/ are introduced for {url}')

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


class LoginScreenIOs(LoginScreenAndroid):
    def __init__(self, app):
        super().__init__(app)

        self.login_screen_clear = (MobileBy.ACCESSIBILITY_ID, 'Clear text')
        self.login_screen_url = (MobileBy.ACCESSIBILITY_ID, 'WebSiteTextField')
        self.login_screen_usrnm = (MobileBy.ACCESSIBILITY_ID, 'UsernameTextField')
        self.login_screen_psswrd = (MobileBy.ACCESSIBILITY_ID, 'PasswordTextField')
        self.login_screen_save_psswrd = (MobileBy.ACCESSIBILITY_ID, 'KeepPasswordSwitch')
        self.login_button = (MobileBy.ACCESSIBILITY_ID, 'LoginButton')
        self.app_version = (MobileBy.ACCESSIBILITY_ID, 'Horizontal scroll bar, 1 page')

    def save_psswrd(self):
        selected = self.app.wait_element(self.login_screen_save_psswrd).get_attribute('value')

        if selected == '1':
            print('Password already saved')
        else:
            self.app.wait_element(self.login_screen_save_psswrd).click()
            print('- Saving the Password')
