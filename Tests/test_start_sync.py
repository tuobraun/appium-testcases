import pytest
import allure


#@pytest.mark.skip(reason='No Sync needed')
@allure.title('App can sync data from drawer menu')
def test_sync_from_drawer(mainfixture):
    #mainfixture.sync.just_sync()
    mainfixture.dash.open_drawer()
    mainfixture.dash.drawer_actions('Download Changes')
    mainfixture.sync.sync_condition()

@allure.title('App can sync data from bottom navigation bar')
def test_sync_from_bar(mainfixture):
    mainfixture.sync.just_sync()
    mainfixture.sync.sync_condition()
