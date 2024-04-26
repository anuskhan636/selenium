from selenium import webdriver
import os

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://vativeapps.com")

# Take a screenshot
screenshot_path = os.path.join("allure-results", "screenshot.png")
driver.save_screenshot(screenshot_path)

# Quit the WebDriver
driver.quit()
