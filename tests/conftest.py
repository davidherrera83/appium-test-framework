import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from the_internet.herokuapp import Herokuapp


"""
Driver

"""
@pytest.fixture(scope="module")
def driver():
    # Define desired capabilities for the Android emulator with Chrome
    capabilities = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "browserName": "Chrome",
        "automationName": "UiAutomator2",
        "chromedriverExecutableDir": "/opt/homebrew/lib/node_modules/appium-chromedriver/chromedriver/mac/",
        "chromedriverChromeMappingFile": "/opt/homebrew/lib/node_modules/appium-chromedriver/chromedriver/chromedriver_mapping.json",
        "chromedriverAutodownload": True
    }
    
    # Convert capabilities to AppiumOptions instance
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

    # Connect to Appium server and start a session
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723', options=capabilities_options)
    yield driver
    driver.quit()

    """
    Class Instances
    
    """

@pytest.fixture
def herokuapp(driver):
    return Herokuapp(driver)