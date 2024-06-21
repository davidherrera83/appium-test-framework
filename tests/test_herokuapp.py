from fw import Examples


def test_navigate_to_herokuapp(herokuapp, driver):
    herokuapp.visit_herokuapp()
    assert driver.title == "The Internet"
    
def test_click_on_example(herokuapp, driver):
    herokuapp.visit_herokuapp()
    herokuapp.click_on_example(Examples.ADD_REMOVE_ELEMENTS)
    herokuapp.wait_for_url(url_contains="add_remove_elements")
    assert 'add_remove_elements' in driver.current_url, "URL does not contain 'add_remove_elements'"

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
    assert column_a_text == 'A', f"Expected column A to contain 'A' but found '{column_a_text}'"
    assert column_b_text == 'B', f"Expected column B to contain 'B' but found '{column_a_text}'"

    # Drag #column-a to #column-b
    herokuapp.drag_and_drop("#column-a", "#column-b")

    # Verify that the columns switched sides
    column_a_text = herokuapp.get_column_text("#column-a")
    column_b_text = herokuapp.get_column_text("#column-b")

    assert column_a_text == 'B', f"Expected column A to contain 'B' but found '{column_a_text}'"
    assert column_b_text == 'A', f"Expected column B to contain 'A' but found '{column_b_text}'"
