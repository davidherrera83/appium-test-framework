from fw import Examples
from selenium.webdriver.remote.webelement import BaseWebElement

def test_drag_and_drop(herokuapp):
    # Navigate to https://the-internet.herokuapp.com/
    herokuapp.visit_herokuapp()

    # Click on a[href="/drag_and_drop"]
    herokuapp.click_on_example(Examples.DRAG_AND_DROP)

    # Wait for the page to load by checking for the presence of "column-a" and "column-b"
    # Get the text from "column-a" and "column-b"
    # Verify that the columns are in their original order

    herokuapp.wait_for_element_on_page("#column-a")
    herokuapp.wait_for_element_on_page("#column-b")
    column_a_text = herokuapp.get_column_text("#column-a")
    column_b_text = herokuapp.get_column_text("#column-b")
    assert column_a_text == 'A', f"Expected column A to contain 'A' but found '{
        column_a_text}'"
    assert column_b_text == 'B', f"Expected column B to contain 'B' but found '{
        column_a_text}'"

    # Drag #column-a to #column-b
    herokuapp.drag_and_drop("#column-a", "#column-b")

    # Verify that the columns switched sides
    column_a_text = herokuapp.get_column_text("#column-a")
    column_b_text = herokuapp.get_column_text("#column-b")

    assert column_a_text == 'B', f"Expected column A to contain 'B' but found '{
        column_a_text}'"
    assert column_b_text == 'A', f"Expected column B to contain 'A' but found '{
        column_b_text}'"


def test_secure_login(herokuapp):
    herokuapp.visit_herokuapp()
    herokuapp.click_on_example(Examples.FORM_AUTHENTICATION)
    herokuapp.wait_for_element_on_page("#username")
    herokuapp.secure_login()
    success_message = herokuapp.login_successful()

    assert success_message is True

