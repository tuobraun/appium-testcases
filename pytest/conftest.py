import pytest
import allure
from Application.baseApp import App


@pytest.fixture(scope="session")
def mainfixture():
    app = App()
    yield app
    app.destroy()
