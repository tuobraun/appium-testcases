import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class SyncScreenAndroid:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.wait = self.app.wait

        pckgnm = 'com.icertainty.forms:id/'

        #PROFILE SCREEN Locators:
        self.search_clear = (MobileBy.ID, pckgnm+'ListFragment_CancelSearchButton')
        self.search_box = (MobileBy.ID, pckgnm+'ListFragment_Keywords')

        #SYNС
        self.sync_bar = (MobileBy.ID, pckgnm+'StatusBar_Root')
        self.sync_bar_close = (MobileBy.ID, pckgnm+'StatusBar_CloseBtn')
        self.sync_text = (MobileBy.ID, pckgnm+'StatusBarView_MessageTextView')
        self.sync_progress_bar = (MobileBy.ID, pckgnm+'StatusBarView_ProgressBar')
        self.sync_message = (MobileBy.ID, 'android:id/message')
        self.sync_btn_later = (MobileBy.ID, 'android:id/button2')
        self.sync_btn_install = (MobileBy.ID, 'android:id/button1')

        #Dashboard
        self.hamburder_menu = (MobileBy.ID, pckgnm+'HeaderPanelView_MainMenuButton')
        self.dashboard_rght_btn = (MobileBy.ID, pckgnm+'HeaderPanelView_RightButton2')


    def update_check(self, profile_name):
        print('- Starting sync...')
        time.sleep(2)
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Close")')
        try:
            time.sleep(2)
            self.app.find_element(self.sync_btn_later).click()            
            print('WARNING: Please, update the App to the relevant version first!')
        except NoSuchElementException:
            print('- No update needed')
            try:
                self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+profile_name+'")').click()
                print(f'- Profile {profile_name} chosen')
            except NoSuchElementException:
                print('- Default profile is used')
                print('- Waiting for syncing to finish')

    def sync_save_audit(self):
        self.app.find_element(self.hamburder_menu).click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Save Audits")').click()
        try:
            self.app.find_element(self.sync_message)
            print('Sync Error!')
        except NoSuchElementException:
            self.app.wait_element(MobileBy.ID, self.sync_bar_close)
            print("- Starting Sync...")
            self.wait.until(EC.invisibility_of_element_located((MobileBy.ID, self.sync_bar)))
            print("- Sync finished!")

    def just_sync(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Sync")').click()
        time.sleep(60) #Temp Solution. Under re-build due to App changes
        try:
            self.app.find_element(self.sync_message)
            self.app.find_element(self.sync_btn_install).click()
            print('Sync Error!')
        except NoSuchElementException:
            self.app.wait_element(MobileBy.ID, self.sync_bar_close)
            print("- Starting Sync...")
            self.wait.until(EC.invisibility_of_element_located((MobileBy.ID, self.sync_bar)))
            print("- Sync finished!")


class SyncScreenIOs(SyncScreenAndroid):
    def __init__(self, app):
        super().__init__(app)

        #PROFILE SCREEN Locators:
        self.sync_profiles = (MobileBy.ACCESSIBILITY_ID, 'Profiles')

        #SYNС
        self.sync_progress_bar = (MobileBy.ACCESSIBILITY_ID, 'Progress')

    def update_check(self, profile_name):
        print('- Starting sync...')
        time.sleep(3)
        try:
            self.app.find_element(self.sync_profiles)
            print('- Choosing profile...')

            self.app.find_element((MobileBy.ACCESSIBILITY_ID, profile_name)).click()
            print(f'- Profile {profile_name} chosen')

        except NoSuchElementException:
            print('- Default profile is used')
            print('- Waiting for syncing to finish')
