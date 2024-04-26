import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@allure.feature("Website Login")
def test_vative_screenshot():
    """
    This test opens https://vativeapps.com, takes a screenshot, and generates an Allure report.
    """
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    allure.attach(driver.get_screenshot_as_png(), name="Vative Apps Homepage", attachment_type=AttachmentType.PNG)

    try:
        # Simulate website login steps here if applicable (replace with your actual login logic)
        # ...

        # Add assertion to verify successful login (if applicable)
        # assert some_condition

    except Exception as e:
        allure.attach(driver.get_screenshot_as_png(), name="Login Error Screenshot", attachment_type=AttachmentType.PNG)
        raise e

    finally:
        driver.quit()
