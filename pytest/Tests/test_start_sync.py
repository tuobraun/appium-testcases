import pytest
import allure


@allure.title('App can sync data')
def test_start_sync(mainfixture):
    mainfixture.sync.just_sync()
