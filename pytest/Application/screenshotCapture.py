import os
import time

class GetScreenshot:
    def get_screenshot(self):
        self.driver = self.driver
        self.scrn_time = time.strftime('%Y-%m-%d - %H-%M-%S')
        self.currentpath = os.getcwd()
        self.filepath = os.path.join(f'{self.currentpath}/screen-shots/{self.scrn_time} - test screenshot.png')
        self.driver.save_screenshot(self.filepath)
        print(f'Screenshot saved to {self.filepath}')
