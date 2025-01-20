import pytest
from selenium import webdriver
import pytest_html
import pytest_metadata

@pytest.fixture()
def setup(browser):
    if browser == 'Ie':
        driver = webdriver.Ie()
        driver.implicitly_wait(5)
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    else:
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## Pytest HTML report ######################
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)






