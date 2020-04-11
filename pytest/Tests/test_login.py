import pytest
from Credentials.credentials import Credentials


def test_login(mainfixture):
    mainfixture.login.enter_credentials(Credentials.web_site_url, Credentials.user_name, Credentials.password)
    mainfixture.login.save_psswrd()
    mainfixture.login.click_login()

def test_check_upd_profile(mainfixture):
    mainfixture.sync.choose_profile(Credentials.profile_name)

def test_dashboard_loaded(mainfixture):
    mainfixture.dash.dashboard_loaded()
