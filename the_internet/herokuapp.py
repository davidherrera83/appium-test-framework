import re
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Herokuapp:
    """
    Herokuapp Wrapper
    Args:
        driver: Instance of Webdriver driver to use for this session.
    """
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def visit_herokuapp(self):
        self.driver.get("https://the-internet.herokuapp.com/")

        return self
    
    def click_on_example(self, available_example: str):
         example_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, available_example))
            )
         example_link.click()

         return self
    
    def wait_for_page(self, url_contains: str):
        case_insensitive_url = re.compile(url_contains, re.IGNORECASE)
        WebDriverWait(self.driver, 10).until(
            EC.url_matches(case_insensitive_url)
        )

        return self