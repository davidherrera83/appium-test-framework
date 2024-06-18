from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fw import Examples


def test_navigate_to_herokuapp(herokuapp, driver):
    herokuapp.visit_herokuapp()
    assert driver.title == "The Internet"
    
def test_click_on_example(herokuapp, driver):
    herokuapp.visit_herokuapp()
    herokuapp.click_on_example(Examples.ADD_REMOVE_ELEMENTS)
    herokuapp.wait_for_page("add_remove_elements")
    assert 'add_remove_elements' in driver.current_url, "URL does not contain 'add_remove_elements'"