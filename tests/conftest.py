import pytest
import fw
from appium import webdriver
from appium.options.android import UiAutomator2Options
from the_internet.herokuapp import Herokuapp


@pytest.fixture(scope="module")
def driver():
    """
    Set up and tear down the Appium WebDriver for an Android emulator using Chrome. This fixture is scoped to the module level, meaning the WebDriver instance will be shared 
    across all tests in the module.

    :return: An initialized Appium WebDriver instance for the Android emulator using Chrome.
    """
    capabilities = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "browserName": "Chrome",
        "automationName": "UiAutomator2",
        "chromedriverExecutableDir": "/opt/homebrew/lib/node_modules/appium-chromedriver/chromedriver/mac/",
        "chromedriverChromeMappingFile": "/opt/homebrew/lib/node_modules/appium-chromedriver/chromedriver/chromedriver_mapping.json",
        "chromedriverAutodownload": True
    }
    

    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', options=capabilities_options)
    yield driver
    driver.quit()

@pytest.fixture
def user():
    """
    Instance of user which reads from users.json to set user for each test.
    """
    _user = fw.get_user()

    return _user


@pytest.fixture
def herokuapp(driver, user):
    """
    Instance of HerokuApp for each test.
    """
    _herokuapp = Herokuapp(driver, user)
    return _herokuapp
