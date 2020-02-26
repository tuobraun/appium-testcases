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

    def dashboard_loaded(self):
        self.wait.until(EC.element_to_be_clickable((MobileBy.ID, self.dashboard_rght_btn)))
        print('- Dashboard loaded! :-)')

    def open_section(self, name):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+name+'")').click()
        print(name)
