import pytest
from Credentials.credentials import Credentials


def test_open_settings(mainfixture):
    mainfixture.dash.dashboard_loaded()
    mainfixture.settings.open_drawer()
    mainfixture.settings.open_settings()

def test_assert_url(mainfixture):
    mainfixture.settings.assert_url(Credentials.web_site_url)
    
def test_assert_user(mainfixture):
    mainfixture.settings.assert_user(Credentials.user_name)

def test_reset_data(mainfixture):
    mainfixture.settings.click_reset()
    mainfixture.sync.choose_profile(Credentials.profile_name)
    mainfixture.dash.dashboard_loaded()
