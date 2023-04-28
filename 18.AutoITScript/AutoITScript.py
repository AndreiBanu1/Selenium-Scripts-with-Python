import os
import time
from selenium import webdriver

driver_path = "/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver"
autoit_path = "/Users/banuandreicristian/Documents/AutoIT/Auto"

# Set the path for geckodriver and launch Firefox
driver = webdriver.Firefox(executable_path=driver_path)
URL = "http://localhost:5000/easytesting"
driver.get(URL)
driver.maximize_window()
driver.implicitly_wait(10)

# Run the AutoIT script using subprocess
os.system(f"{autoit_path}.exe")

# Navigate to a webpage
driver.get("https://the-internet.herokuapp.com/basic_auth")

# Close the browser after waiting for 5 seconds
time.sleep(5)
driver.quit()
