import os
import time
import allure
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Application.configurationLoader import load_config
from Screens.screen_login import LoginScreenAndroid, LoginScreenIOs
from Screens.screen_sync import SyncScreenAndroid, SyncScreenIOs
from Screens.screen_dashboard import DashboardScreenAndroid, DashboardScreenIOs
from Screens.screen_settings import SettingsScreenAndroid, SettingsScreenIOs
from Screens.screen_audit import AuditScreenAndroid, AuditScreenIOs

class App:

    def __init__(self, define_platform):
        APPIUM_HOST = 'http://localhost:4723/wd/hub'
        DESIRED_CAPS = load_config(define_platform)

        self.driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS)
        self.wait = WebDriverWait(self.driver, 60)
        self.driver.implicitly_wait(2)
        print('Driver started')

        if define_platform == 'Android':
            self.login = LoginScreenAndroid(self)
            self.sync = SyncScreenAndroid(self)
            self.dash = DashboardScreenAndroid(self)
            self.settings = SettingsScreenAndroid(self)
            self.audit = AuditScreenAndroid(self)
        else:
            self.login = LoginScreenIOs(self)
            self.sync = SyncScreenIOs(self)
            self.dash = DashboardScreenIOs(self)
            self.settings = SettingsScreenIOs(self)
            self.audit = AuditScreenIOs(self)

        self.driver.hide_keyboard()

    def destroy(self):
        self.driver.close_app()
        self.driver.quit()

    # Custom Find methods
    def wait_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def wait_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    #Helpers
    def get_screenshot(self):
        self.scrn_time = time.strftime('%Y-%m-%d_-_%H-%M-%S')
        self.currentpath = os.getcwd()
        self.filepath = os.path.join(f'{self.currentpath}/screen-shots/{self.scrn_time} - test screenshot.png')
        self.driver.save_screenshot(self.filepath)
        print(f'Screenshot saved to {self.filepath}')
        allure.attach.file(f'{self.filepath}', attachment_type=allure.attachment_type.PNG)
