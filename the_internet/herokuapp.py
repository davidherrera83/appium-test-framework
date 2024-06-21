from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException


class Herokuapp:
    def __init__(self, driver: WebDriver):
        """
        Initialize the Herokuapp class with a WebDriver instance.

        :param driver: The WebDriver instance used to interact with the browser.
        """
        self.driver = driver

    def visit_herokuapp(self):
        """
        Navigate to the Herokuapp home page.
        """
        self.driver.get("https://the-internet.herokuapp.com/")

        return self

    def click_on_example(self, available_example: str):
        """
        Click on an example link identified by its CSS selector.

        :param css_selector: The CSS selector of the element to wait for.
        """
        example_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, available_example))
        )
        example_link.click()

        return self

    def wait_for_element_on_page(self, css_selector: str):
        """
        Wait for the presence of an element identified by its CSS selector.

        :param css_selector: The CSS selector of the element to wait for.
        :raises TimeoutException: If the element does not appear within the timeout period.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )

            return self

        except TimeoutException:
            raise TimeoutException(
                f"Timeout waiting for page with element CSS_SELECTOR={css_selector}")

    def get_column_text(self, css_selector: str):
        """
        Gets the text within a column identified by its CSS selector.

        :param css_selector: The CSS selector of the element to wait for.
        """
        try:
            colummn_name = self.driver.find_element(
                By.CSS_SELECTOR, css_selector).text

            return colummn_name

        except TimeoutError:
            raise TimeoutException(
                f"Timeout waiting for element CSS_SELECTOR={css_selector}")

    def drag_and_drop(self, source_css_selector: str, target_css_selector: str):
        """
        Perform a drag-and-drop action from a source element to a target element.

        :param source_css_selector: The CSS selector of the source element.
        :param target_css_selector: The CSS selector of the target element.
        """
        source_element = self.driver.find_element(
            By.CSS_SELECTOR, source_css_selector)
        target_element = self.driver.find_element(
            By.CSS_SELECTOR, target_css_selector)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()

        return self
