import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@allure.feature("Website Login")
def test_vative_screenshot():
  """
  This test opens a specific page on vativeapps.com, takes a screenshot, and generates an Allure report.
  """
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

  # Navigate to the desired page on vativeapps.com
  driver.get("https://vativeapps.com/")  # Replace with the actual URL

  allure.attach(driver.get_screenshot_as_png(), name="Vative Apps - Specific Page", attachment_type=AttachmentType.PNG)

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
