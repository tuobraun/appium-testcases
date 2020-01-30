from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Driver:

    def __init__(self):
        desired_caps = {            
            "platformName": "Android",
            "platformVersion": "10",
            "deviceName": "Pixel_2",
            #"app": "C:/Users/vsergin/OneDrive - ICertainty/Appium/apks/com.icertainty.forms_7.0.458_r.apk",
            "noReset": "false",
            #"fullReset": "true",
            "appPackage": "com.icertainty.forms",
            "appActivity": "crc640126a6b348a6ad42.MainActivity",
            "automationName": "uiautomator2",
            "skipDeviceInitialization": "true", #set to false/comment when first time
            "skipServerInstallation": "true", #set to false/comment when first time
            "isHeadless": "true",
            "disableAndroidWatchers": "true",
            "skipUnlock": "true",
            "disableWindowAnimation": "true",
            "autoGrantPermissions ": "true",
            #"clearDeviceLogsOnStart": True,
            #"unicodeKeyboard": True,
            #"resetKeyboard": True
        }
        
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.wait = WebDriverWait(self.instance, 120)
