import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="module")
def driver():
    # Define desired capabilities for the Android emulator with Chrome
    capabilities = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "browserName": "Chrome",
        "automationName": "UiAutomator2"
    }
    # Convert capabilities to AppiumOptions instance
    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    
    # Connect to Appium server and start a session
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub', options=capabilities_options)
    driver.implicitly_wait(10)  # seconds
    yield driver
    # Teardown: Quit the driver
    driver.quit()