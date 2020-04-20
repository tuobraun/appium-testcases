import pytest
import allure
from Credentials.credentials import Credentials

@allure.title('Login credentials can be typped in')
def test_login(mainfixture):
    mainfixture.login.enter_credentials(Credentials.web_site_url, Credentials.user_name, Credentials.password)
    mainfixture.login.save_psswrd()
    mainfixture.login.click_login()

@allure.title('Mobile profile can be chosen')
def test_check_upd_profile(mainfixture):
    mainfixture.sync.choose_profile(Credentials.profile_name)

@allure.title('Dashboard can be loaded')
def test_dashboard_loaded(mainfixture):
    mainfixture.dash.dashboard_loaded()
