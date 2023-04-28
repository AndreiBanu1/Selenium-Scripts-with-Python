from selenium import webdriver
import time

# Set path to GeckoDriver executable
driver_path = "/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver"
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--start-maximized")

# Initialize the Firefox browser
driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)

# Load properties from file
with open("/Users/banuandreicristian/Documents/id", "r") as prop_file:
    properties = dict(line.strip().split("=") for line in prop_file)

# Navigate to the base URL
driver.get(properties["baseURL"])

# Fill in login credentials
driver.find_element_by_xpath(properties["email_field"]).send_keys(properties["email"])
driver.find_element_by_xpath(properties["password_field"]).send_keys(properties["password"])

# Click the login button
driver.find_element_by_xpath(properties["btn"]).click()

# Wait for 3 seconds before closing the browser
time.sleep(3)
driver.quit()
