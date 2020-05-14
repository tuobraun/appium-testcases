import os
import time
from Credentials.credentials import Credentials, FtpCredentials
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_argument('headless')

currentpath = os.getcwd()
configpath = os.path.join(f'{currentpath}/apps/{FtpCredentials.CONFIG_NAME}.xml')

driver = webdriver.Chrome(executable_path=f'{currentpath}/webdriver/chromedriver.exe', options=options)
#driver.maximize_window()

wait = WebDriverWait(driver, 30)

print('- Starting browser')

driver.get(Credentials.profile_url)

driver.find_element_by_id('txtUsername').send_keys(Credentials.user_name)
driver.find_element_by_id('txtPassword').send_keys(Credentials.password)
driver.find_element_by_id('logInBtn').click()

time.sleep(5)
driver.switch_to.frame('ifrMain')
driver.find_element_by_id('ASPxPageControlMain_T1').click()

wait.until(EC.visibility_of_element_located((By.ID, 'inpSettingsFile'))).send_keys(configpath)
print(f'- Inserted xml: {configpath}')

driver.find_element_by_id('btnSave_CMD').click()

time.sleep(7)
print('- Done!')

driver.quit()
