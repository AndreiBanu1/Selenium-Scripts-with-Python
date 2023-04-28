from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

# Setting up ChromeDriver
chrome_driver_path = "/Users/banuandreicristian/Documents/WebDrivers/chromedriver/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Maximizing window and waiting for the page to load
driver.maximize_window()
driver.implicitly_wait(10)

# Alert message handling
driver.get("http://localhost:5000/easytesting")
driver.find_element(By.ID, "submit").click()

# Switching to Alert
alert = Alert(driver)

# Sending data to the alert box
alert.send_keys("Andrei")
time.sleep(1)

# Capturing alert message
alert_message = alert.text

# Displaying alert message
print(alert_message)

# Waiting and accepting the alert
time.sleep(5)
alert.accept()

# Quitting the driver
driver.quit()
