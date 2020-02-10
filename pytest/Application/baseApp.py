from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Screens.screen_login import LoginScreen
from Screens.screen_sync import SyncScreen

class App:

    def __init__(self, platform='android'):
        DESIRED_CAPS = None
        APPIUM_HOST = 'http://localhost:4723/wd/hub'
        BUNDLE_NAME = 'com.icertainty.forms'
        #PCKGNM = BUNDLE_NAME+':id/'

        #MY_APP_ANDROID = 'D:/OneDrive - ICertainty/Appium/Projects/WAWA Auditing - POM - pytest - NEW/apps/latest.apk'
        #MY_APP_IOS = './apps/latest.ipa'

        DESIRED_CAPS_ANDROID = {
            'platformName': 'android',
            'platformVersion': '10',
            'deviceName': 'Pixel_C',
            'noReset': 'false',
            'appPackage': BUNDLE_NAME,
            'appActivity': 'crc640126a6b348a6ad42.MainActivity',
            'automationName': 'uiautomator2',
            'skipDeviceInitialization': 'true',  # set to false/comment when run first time
            'skipServerInstallation': 'true',  # set to false/comment when run first time
            'isHeadless': 'true',
            'disableAndroidWatchers': 'true',
            'skipUnlock': 'true',
            'disableWindowAnimation': 'true',
            'autoGrantPermissions ': 'true',
            #'app': MY_APP_ANDROID,
            #'fullReset': 'true',
            #'clearDeviceLogsOnStart': True,
            #'resetKeyboard': True
        }

        DESIRED_CAPS_IOS = {
            'platformName': 'iOS',
            'platformVersion': '13.3.1',
            'deviceName': 'iPhone 7',
            #'app': MY_APP_IOS
        }
        self.platform = platform
        if platform == 'android':
            DESIRED_CAPS = DESIRED_CAPS_ANDROID
        else:
            DESIRED_CAPS = DESIRED_CAPS_IOS

        self.driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS)
        self.wait = WebDriverWait(self.driver, 120)
        self.driver.implicitly_wait(2)

        self.login = LoginScreen(self)
        self.sync = SyncScreen(self)


    def destroy(self):
        self.driver.quit()

    # Custom Find methods
    def wait_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def wait_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def find_element(self, locator):
        return self.driver.find_element(*locator)
