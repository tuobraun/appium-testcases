import os
import time


def get_screenshot(self):
    self.scrn_time = time.strftime('%Y-%m-%d - %H-%M-%S')
    self.currentpath = os.getcwd()
    self.filepath = os.path.join(f'{self.currentpath}/{self.scrn_time} - test screenshot.png')
    self.driver.save_screenshot(self.filepath)
    print(f'Screenshot saved to {self.filepath}')
