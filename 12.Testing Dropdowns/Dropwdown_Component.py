from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Setting up ChromeDriver
chrome_driver_path = "/Users/banuandreicristian/Documents/WebDrivers/chromedriver/chromedriver"
driver = webdriver.Chrome(chrome_driver_path)

# Maximizing window and waiting for the page to load
driver.maximize_window()
driver.implicitly_wait(10)

# Navigating to the website
driver.get("http://localhost:5000/dropdown")

# Extracting all options from the dropdown menu and printing them
cars = Select(driver.find_element(By.ID, "cars"))
options = cars.options
for option in options:
    print(option.text)

# Waiting and quitting the driver
time.sleep(10)
driver.quit()
