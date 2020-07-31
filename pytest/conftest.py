import platform
import pytest
from Application.baseApp import App


@pytest.fixture(scope="session")
def mainfixture(define_platform):
    app = App(define_platform)
    yield app
    app.get_screenshot()
    app.destroy()

@pytest.fixture(scope="session")
def define_platform():
    pl = platform.system()
    platform_name = 'Android' if pl == 'Windows' else 'iOS'
    return platform_name
