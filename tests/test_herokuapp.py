def test_navigate_and_assert_title(driver):
    # Navigate to the URL
    driver.get("https://the-internet.herokuapp.com/")
    # Assert the title is 'The Internet'
    assert driver.title == "The Internet"
