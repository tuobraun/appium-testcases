from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Screens.screen_login import LoginScreenAndroid, LoginScreenIOs
from Screens.screen_sync import SyncScreenAndroid
from Screens.screen_dashboard import DashboardScreenAndroid, DashboardScreenIOs
from Screens.screen_audit import AuditScreenAndroid, AuditScreenIOs

class App:

    def __init__(self, platform='android'):
        DESIRED_CAPS = None
        APPIUM_HOST = 'http://localhost:4723/wd/hub'
        BUNDLE_NAME = 'com.icertainty.forms'

        #MY_APP_ANDROID = 'apps/latest.apk'
        #MY_APP_IOS = '/Users/tuobraun/Documents/projects/icertainty.forms-v7.0.489/ICertainty.Forms.iOSApp/bin/iPhoneSimulator/Debug/device-builds/iphone 11 pro max-13.3/ICertaintyFormsiOSApp.app'

        DESIRED_CAPS_ANDROID = {
            'platformName': 'android',
            'platformVersion': '10',
            'deviceName': 'Pixel_С',
            'noReset': 'false',
            'appPackage': BUNDLE_NAME,
            'appActivity': 'crc640126a6b348a6ad42.MainActivity', #x86 build
            #'appActivity': 'md5e4cac7e579ae8e4a79268355e7889b69.MainActivity', #ARM build
            'automationName': 'uiautomator2',
            'skipDeviceInitialization': 'true',  # set to false/comment when run first time
            'skipServerInstallation': 'true',  # set to false/comment when run first time
            'isHeadless': 'true',
            'disableAndroidWatchers': 'true',
            'skipUnlock': 'true',
            'disableWindowAnimation': 'true',
            'autoGrantPermissions ': 'true',
            #'clearSystemFiles': 'true',
            #'clearDeviceLogsOnStart': True,
            #'app': MY_APP_ANDROID,
            #'fullReset': 'true',
            #'resetKeyboard': True
        }

        DESIRED_CAPS_IOS = {
            'platformName': 'iOS',
            'platformVersion': '13.2',
            'automationName': 'XCUITest',
            'deviceName': 'iPhone 11 Pro Max',
            #'useNewWDA': 'true',
            'bundleId': 'com.ICertainty.Forms',
            'udid': 'auto',
            'noReset': 'true',
            'clearSystemFiles': 'true'
            #'app': MY_APP_IOS
        }

        self.platform = platform
        if platform == 'android':
            DESIRED_CAPS = DESIRED_CAPS_ANDROID
        else:
            DESIRED_CAPS = DESIRED_CAPS_IOS

        self.driver = webdriver.Remote(APPIUM_HOST, DESIRED_CAPS)
        self.wait = WebDriverWait(self.driver, 90)
        self.driver.implicitly_wait(2)

        if platform == 'android':
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
        self.driver.quit()

    # Custom Find methods
    def wait_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def wait_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator), message=f"Can't find elements by locator {locator}")

    def find_element(self, locator):
        return self.driver.find_element(*locator)
