import pytest
import allure


@pytest.mark.skip(reason='No Sync needed')
@allure.title('App can sync data')
def test_start_sync(mainfixture):
    mainfixture.sync.just_sync()
