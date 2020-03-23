from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Application.configurationLoader import load_config
from Screens.screen_login import LoginScreenAndroid, LoginScreenIOs
from Screens.screen_sync import SyncScreenAndroid
from Screens.screen_dashboard import DashboardScreenAndroid, DashboardScreenIOs
from Screens.screen_audit import AuditScreenAndroid, AuditScreenIOs

class App:

    def __init__(self, platform='iOS'):
        APPIUM_HOST = 'http://localhost:4723/wd/hub'
        DESIRED_CAPS = load_config()

        self.driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS)
        self.wait = WebDriverWait(self.driver, 90)
        self.driver.implicitly_wait(2)
        print('Driver started')

        if platform == 'Android':
            self.login = LoginScreenAndroid(self)
            self.sync = SyncScreenAndroid(self)
            self.dash = DashboardScreenAndroid(self)
            self.audit = AuditScreenAndroid(self)
        else:
            self.login = LoginScreenIOs(self)
            self.dash = DashboardScreenIOs(self)
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
