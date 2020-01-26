import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BaseFunctions(object):
    def __init__(self, driver):
        self.driver = driver
        #pckgnm = "com.icertainty.forms:id/"

    def click_button(self, locator_id):
        pass

# IN DEVELOPMENT. NOT USED