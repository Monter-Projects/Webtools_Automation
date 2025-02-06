import pytest
from selenium import webdriver
import pytest_html
import pytest_metadata

from selenium.webdriver.chrome.options import Options


chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")  # Ensure a full-screen size
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")  # By
@pytest.fixture()
def setup(browser):
    if browser == 'Ie':
        driver = webdriver.Ie()
        driver.implicitly_wait(10)
    elif browser == 'Chrome':
        driver = webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(10)
    else:
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
    return driver

@pytest.fixture()
def url(IP):
    url = "https://" + IP + "/wt4/home"
    return url

def pytest_addoption(parser):
    parser.addoption("--IP", action="store", default="dev", help="Environment: Server-IP")
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def IP(request):
    return request.config.getoption("--IP")



########## Pytest HTML report ######################
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)






