import os
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def browser():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(browser):
    try:
        # Navigate to the website
        browser.get("https://vativeapps.com")

        # Take a screenshot
        screenshot_path = os.path.join("allure-results", "screenshot.png")
        browser.save_screenshot(screenshot_path)

        # Your test steps here
        
        # Example: Assert title
        assert "Expected Title" in browser.title

    except Exception as e:
        # Handle exceptions, e.g., print error message
        print("An error occurred:", e)
        raise e
