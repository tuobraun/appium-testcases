from appium.webdriver.common.mobileby import MobileBy
from Credentials.credentials import Credentials


class SettingsScreenAndroid():
    
    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.wait = self.app.wait

        self.hamburder_menu = (MobileBy.ID, 'HeaderPanelView_MainMenuButton')

        self.drawer_sync = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="ListItemViewHolder:2"]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.ImageView')
        self.drawer_settings = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="ListItemViewHolder:3"]/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.ImageView')

        self.web_site_url = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="ValueViewHolder:2"]/android.widget.LinearLayout/android.widget.TextView[2]')
        self.current_user = (MobileBy.XPATH, '//android.widget.LinearLayout[@content-desc="ValueViewHolder:4"]/android.widget.LinearLayout/android.widget.TextView[2]')

        self.reset_data = (MobileBy.ACCESSIBILITY_ID, 'ButtonViewHolder:9_ResetData')
        self.sync_btn_install = (MobileBy.ID, 'android:id/button1')

    def open_drawer(self):
        self.app.wait_element(self.hamburder_menu).click()

    def drawer_actions(self, drawerAction):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+drawerAction+'")').click() 

    def assert_url(self):
        current_url = self.app.wait_element(self.web_site_url).text
        return current_url

    def assert_user(self):
        current_username = self.app.wait_element(self.current_user).text
        s = current_username
        s = s[s.find('(')+1:s.find(')')]
        return s

    def click_reset(self):
        self.app.wait_element(self.reset_data).click()
        self.app.wait_element(self.sync_btn_install).click()


class SettingsScreenIOs(SettingsScreenAndroid):
    def __init__(self, app):
        super().__init__(app)

        self.hamburder_menu = (MobileBy.ACCESSIBILITY_ID, 'MainMenu-Button')
        self.web_site_url = (MobileBy.ACCESSIBILITY_ID, Credentials.web_site_url) #Not true :(
        self.current_user = (MobileBy.ACCESSIBILITY_ID, 'Sergin, Vadim (vsergin) ') #Not true :(
        self.reset_data = (MobileBy.ID, 'Reset Data')
        self.sync_btn_install = (MobileBy.XPATH, '//XCUIElementTypeButton[@name="Reset"]')

    def drawer_actions(self, drawerAction):
        self.app.wait_element((MobileBy.ACCESSIBILITY_ID, drawerAction)).click()
    
    def assert_url(self):
        current_url = self.app.wait_element(self.web_site_url).text
        return current_url

    def assert_user(self):
        current_username = self.app.wait_element(self.current_user).text
        s = current_username
        s = s[s.find('(')+1:s.find(')')]
        return s
