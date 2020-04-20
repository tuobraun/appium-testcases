import pytest
import allure
from Credentials.credentials import Credentials


@allure.step('Step: Opening Settings')
@allure.description("""Opening Settings through the drawer menu""")
@allure.title('Settings Screen can be opened')
def test_open_settings(mainfixture):
    mainfixture.dash.dashboard_loaded()
    mainfixture.settings.open_drawer()
    mainfixture.settings.open_settings()

@allure.step('Asserting credentials')
@allure.description("""Making sure that we logged in to the correct Website""")
@allure.title('Asserting URL')
@allure.severity(allure.severity_level.CRITICAL)
def test_assert_url(mainfixture):
    assert mainfixture.settings.assert_url() == Credentials.web_site_url

@allure.description("""Making sure that we logged in under the correct User""")
@allure.title('Asserting Username')
@allure.severity(allure.severity_level.CRITICAL)
def test_assert_user(mainfixture):
    assert mainfixture.settings.assert_user() == Credentials.user_name

@pytest.mark.skip(reason='No Reset needed. Data must be submitted to the Server')
@allure.step('Step: Reseting Data')
@allure.title('Data can be Reset')
def test_reset_data(mainfixture):
    mainfixture.settings.click_reset()
    mainfixture.sync.choose_profile(Credentials.profile_name)
    mainfixture.dash.dashboard_loaded()
