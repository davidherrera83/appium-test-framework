from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Herokuapp:
    def __init__(self, driver, user):
        """
        Initialize the Herokuapp class.

        Args:
            driver: WebDriver instance.
            user: User object containing login credentials.
        """
        self.driver = driver
        self.user = user
    
    def visit_herokuapp(self):
        """
        Navigate to the Herokuapp main page.

        Returns:
            self: The Herokuapp instance for method chaining.
        """
        self.driver.get("https://the-internet.herokuapp.com/")
        return self
    
    def click_on_example(self, available_example: str):
        """
        Click on a specific example on the Herokuapp main page.

        Args:
            available_example (str): The CSS selector of the example to click.

        Returns:
            self: The Herokuapp instance for method chaining.
        """
        example_link = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, available_example))
        )
        example_link.click()
        return self
    
    def wait_for_element_on_page(self, css_selector: str):
        """
        Wait for an element to be present on the page.

        Args:
            css_selector (str): The CSS selector of the element to wait for.

        Returns:
            self: The Herokuapp instance for method chaining.

        Raises:
            TimeoutException: If the element is not found within the timeout period.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )
            return self
        except TimeoutException:
            raise TimeoutException(f"Timeout waiting for page with element CSS_SELECTOR={css_selector}")
    
    def scroll_down(self):
        """
        Perform a scroll down action on the page.

        This method scrolls the page down by one viewport height and waits
        for the scroll to complete and for new content to load.

        Returns:
            self: The Herokuapp instance for method chaining.
        """
        body = self.driver.find_element(By.TAG_NAME, 'body')
        initial_scroll = self.driver.execute_script("return window.pageYOffset")
        
        actions = ActionChains(self.driver)
        actions.move_to_element(body)
        actions.send_keys(Keys.PAGE_DOWN)
        actions.perform()
        
        # Wait for the page to scroll
        WebDriverWait(self.driver, 5).until(
            lambda driver: driver.execute_script("return window.pageYOffset") > initial_scroll
        )
        
        time.sleep(2)  # Wait for content to load
        return self
    
    def get_number_of_paragraphs(self):
        """
        Get the number of paragraphs loaded on the infinite scroll page.

        Returns:
            int: The number of paragraphs (div.jscroll-added elements) on the page.
        """
        paragraphs = self.driver.find_elements(By.CSS_SELECTOR, "div.jscroll-added")
        return len(paragraphs)
    
    def scroll_down_and_verify(self, scroll_times: int):
        """
        Perform multiple scroll down actions and verify that new content is loaded.

        This method scrolls the page down a specified number of times and checks
        if new content (paragraphs) is loaded after each scroll.

        Args:
            scroll_times (int): The number of times to scroll down and verify.

        Returns:
            bool: True if new content was loaded after each scroll, False otherwise.
        """
        initial_paragraphs = self.get_number_of_paragraphs()
        
        for _ in range(scroll_times):
            self.scroll_down()
            
            try:
                WebDriverWait(self.driver, 10).until(
                    lambda d: self.get_number_of_paragraphs() > initial_paragraphs
                )
            except TimeoutException:
                return False
            
            new_paragraphs = self.get_number_of_paragraphs()
            if new_paragraphs <= initial_paragraphs:
                return False
            
            initial_paragraphs = new_paragraphs
        
        return True

    def get_column_text(self, css_selector: str):
        """
        Gets the text within a column identified by its CSS selector.

        :Args:
            css_selector: The CSS selector of the element to wait for.
        """
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        return element.text

    def drag_and_drop(self, source_selector: str, target_selector: str):
        """
        Perform a drag-and-drop action from a source element to a target element.

        Args: 
            source_css_selector: css selector of the source element.
            target_css_selector: css selector of the target element.
        """
        source = self.driver.find_element(By.CSS_SELECTOR, source_selector)
        target = self.driver.find_element(By.CSS_SELECTOR, target_selector)
        
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source, target).perform()
        return self

    def secure_login(self):
        """
        Users are able to authenticate via secure login page

        Returns:
          self: The Herokuapp instance for method chaining.
        """
        username_field = self.driver.find_element(By.CSS_SELECTOR, "#username")
        password_field = self.driver.find_element(By.CSS_SELECTOR, "#password")
        submit_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        username_field.send_keys(self.user.username)
        password_field.send_keys(self.user.password)
        submit_button.click()
        return self

    def login_successful(self):
        """
        Searches for successful login message.

        Returns: 
            bool : True if the success message is displayed.
        """
        try:
            success_message = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.CSS_SELECTOR, 'div.flash.success'))
            )
            return success_message.is_displayed()
        except TimeoutException:
            return False