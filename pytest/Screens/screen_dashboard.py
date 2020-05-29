from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


class DashboardScreenAndroid:

    def __init__(self, app):
        self.app = app
        self.driver = self.app.driver
        self.wait = self.app.wait

        pckgnm = "com.icertainty.forms:id/"

        #DASHBOARD, PANNEL, LISTVIEWS
        self.dashboard_header = pckgnm+"HeaderPanelView_Title"
        self.dashboard_section = pckgnm+"DetailsFragment_ItemsView"
        self.hamburder_menu = pckgnm+"HeaderPanelView_MainMenuButton"
        self.dashboard_rght_btn = pckgnm+"HeaderPanelView_RightButton2"

        self.back_arrow = pckgnm+"HeaderPanelView_BackButton"
        self.filter_icon = pckgnm+"ActionButtonView_RootLayout"
        self.list_view = pckgnm+"ListItemView_GroupTextView"

        self.footer_new = (MobileBy.ACCESSIBILITY_ID, 'NewFooterButton')
        self.footer_scheduled = (MobileBy.ACCESSIBILITY_ID, 'ScheduleFooterButton')
        self.footer_sync = (MobileBy.ACCESSIBILITY_ID, 'SyncFooterButton')
        self.footer_home = (MobileBy.ACCESSIBILITY_ID, 'HomeFooterButton')

    def dashboard_loaded(self):
        self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.dashboard_rght_btn)))
        print('- Dashboard loaded! :-)')

    def open_section(self, name):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+name+'")').click()
        print(name)


class DashboardScreenIOs(DashboardScreenAndroid):
    def __init__(self, app):
        super().__init__(app)

        self.dashboard_rght_btn = (MobileBy.ACCESSIBILITY_ID, '...')
        self.back_arrow = (MobileBy.ACCESSIBILITY_ID, 'LeftArrow')
        self.filter_icon = (MobileBy.ACCESSIBILITY_ID, 'bit dark filter')
        self.start_new = (MobileBy.ACCESSIBILITY_ID, 'Start New')       

    def dashboard_loaded(self):
        self.app.wait_element(self.dashboard_rght_btn)
        print('- Dashboard loaded! :-)')

    def open_section(self, name):
        self.app.wait_element((MobileBy.ACCESSIBILITY_ID, name)).click()
        print(name)
