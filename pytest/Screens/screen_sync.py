import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class SyncScreen:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.wait = self.app.wait

        pckgnm = "com.icertainty.forms:id/"

        #PROFILE SCREEN Locators:
        self.search_clear = (MobileBy.ID, pckgnm+"ListFragment_CancelSearchButton")
        self.search_box = (MobileBy.ID, pckgnm+"ListFragment_Keywords")

        #SYNС
        self.sync_bar = (MobileBy.ID, pckgnm+"StatusBar_Root")
        self.sync_bar_close = (MobileBy.ID, pckgnm+"StatusBar_CloseBtn")
        self.sync_text = (MobileBy.ID, pckgnm+"StatusBarView_MessageTextView")
        self.sync_progress_bar = (MobileBy.ID, pckgnm+"StatusBarView_ProgressBar")
        self.sync_message = (MobileBy.ID, "android:id/message")
        self.sync_btn_later = (MobileBy.ID, "android:id/button2")
        self.sync_btn_install = (MobileBy.ID, "android:id/button1")

    def update_check(self, profile_name):
        try:
            time.sleep(5)
            self.app.find_element(self.sync_btn_later).click()
            print("WARNING: Please, update the App to the relevant version first!")
        except NoSuchElementException:
            print('- No update needed')
            try:
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+profile_name+'")').click()
                print('- Profile chosen')
            except NoSuchElementException:
                print('- Default profile is used')
                print('- Waiting for syncing to finish')
                self.wait.until(EC.element_to_be_clickable((MobileBy.ID, "com.icertainty.forms:id/HeaderPanelView_RightButton2")))
                time.sleep(5)
                print('- Dashboard loaded! :-)')
