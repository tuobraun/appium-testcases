import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginScreen:
    
    def __init__(self, driver):
        self.driver = driver
        wait = WebDriverWait(self.driver.instance, 120)
        pckgnm = "com.icertainty.forms:id/"

        #LOGIN SCREEN Locators:
        self.login_screen_logo = wait.until(EC.visibility_of_element_located((MobileBy.ID, pckgnm+"LoginFragment_Logo")))
        self.login_screen_url = wait.until(EC.visibility_of_element_located((MobileBy.ID, pckgnm+"LoginFragment_Url")))
        self.login_screen_usrnm = wait.until(EC.visibility_of_element_located((MobileBy.ID, pckgnm+"LoginFragment_UserName")))
        self.login_screen_psswrd = wait.until(EC.visibility_of_element_located((MobileBy.ID, pckgnm+"LoginFragment_Password")))
        self.login_screen_save_psswrd = wait.until(EC.visibility_of_element_located((MobileBy.ID, pckgnm+"LoginFragment_KeepPass")))
        self.login_button = wait.until(EC.visibility_of_element_located((MobileBy.ID, pckgnm+"LoginFragment_LoginBtn")))
        self.app_version = wait.until(EC.visibility_of_element_located((MobileBy.ID, pckgnm+"LoginFragment_VersionNumber")))

    def enter_url(self, url):        
        self.login_screen_url.send_keys(url)
        print(f'Entered URL: {url}')

    def enter_username(self, username):
        self.login_screen_usrnm.send_keys(username)
        print(f'Entered Username: {username}')

    def enter_psswrd(self, psswrd):
        self.login_screen_psswrd.send_keys(psswrd)
        print('Password entered')

    def save_psswrd(self):
        self.selected = self.login_screen_save_psswrd.is_selected()

        if self.selected == True:
            print('Password already saved')
        else:
            self.login_screen_save_psswrd.click()
            print('Saving the Password')

    def click_login(self):
        self.login_button.click()
        print('Trying to login')
