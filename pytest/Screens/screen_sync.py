import time
from datetime import datetime
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class SyncScreenAndroid:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.wait = self.app.wait

        #PROFILE SCREEN Locators:
        self.search_clear = (MobileBy.ID, 'ListFragment_CancelSearchButton')
        self.search_box = (MobileBy.ID, 'ListFragment_Keywords')

        #SYNС
        self.sync_bar = (MobileBy.ID, 'StatusBar_Root')
        self.sync_bar_close = (MobileBy.ID, 'StatusBar_CloseBtn')
        self.sync_text = (MobileBy.ID, 'StatusBarView_MessageTextView')
        self.sync_progress_bar = (MobileBy.ID, 'StatusBarView_ProgressBar')
        self.sync_message = (MobileBy.ID, 'android:id/message')
        self.sync_btn_later = (MobileBy.ID, 'android:id/button2')
        self.sync_btn_install = (MobileBy.ID, 'android:id/button1')

        #Dashboard
        self.hamburder_menu = (MobileBy.ID, 'HeaderPanelView_MainMenuButton')
        self.dashboard_rght_btn = (MobileBy.ID, 'HeaderPanelView_RightButton2')
        self.footer_sync = (MobileBy.ACCESSIBILITY_ID, 'SyncFooterButton')

    def choose_profile(self, profile_name):
        self.wait.until(EC.invisibility_of_element_located((self.sync_bar_close)))
        print('- Starting sync...')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("Profiles")')
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+profile_name+'")').click()
        print(f'- Profile {profile_name} chosen')
        print('- Waiting for syncing to finish')

    def sync_condition(self):
        self.app.wait_element(self.sync_bar_close)
        start_time = datetime.now()
        print("- Starting Sync...")
        self.wait.until(EC.invisibility_of_element_located((self.sync_bar)))
        print("- Sync is in progress...")
        self.wait.until(EC.visibility_of_element_located((self.sync_bar)))
        print(f'Sync finished in: {datetime.now()-start_time}')

    def just_sync(self):
        self.app.find_element(self.footer_sync).click()
        

class SyncScreenIOs(SyncScreenAndroid):
    def __init__(self, app):
        super().__init__(app)

        #PROFILE SCREEN Locators:
        self.sync_profiles = (MobileBy.ACCESSIBILITY_ID, 'Profiles')

        #SYNС
        self.sync_bar = (MobileBy.ACCESSIBILITY_ID, 'StatusBar-View')
        self.sync_info = (MobileBy.ACCESSIBILITY_ID, 'More Info')
        self.sync_bar_close = (MobileBy.ACCESSIBILITY_ID, 'StatusBar-CloseButton')
        self.sync_progress_bar = (MobileBy.ACCESSIBILITY_ID, 'StatusBar-ProgressView')
        self.footer_sync = (MobileBy.ACCESSIBILITY_ID, 'SyncFooterButton')
        self.sync_text = (MobileBy.ACCESSIBILITY_ID, 'StatusBar-MessageLabel')
        self.sync_message = (MobileBy.ACCESSIBILITY_ID, 'The Internet connection failed during the synchronization.The Internet connection appears to be offline.')
        
        #Dashboard
        self.hamburder_menu = (MobileBy.ACCESSIBILITY_ID, 'MainMenu-Button')
        self.dashboard_rght_btn = (MobileBy.ACCESSIBILITY_ID, '...')


    def choose_profile(self, profile_name):
        self.wait.until(EC.invisibility_of_element_located((self.sync_bar_close)))
        print('- Starting sync...')
        self.app.find_element(self.sync_profiles)
        print('- Choosing profile...')
        self.app.find_element((MobileBy.ACCESSIBILITY_ID, profile_name)).click()
        print(f'- Profile {profile_name} chosen')
        print('- Waiting for syncing to finish')
