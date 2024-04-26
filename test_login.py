import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login(browser):
    browser.get("https://vativeapps.com")
    # Your login test steps here
    assert "Expected Title" in browser.title
