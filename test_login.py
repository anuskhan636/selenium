from selenium import webdriver

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://vativeapps.com")

# Take a screenshot
driver.save_screenshot("screenshot.png")

# Quit the WebDriver
driver.quit()
