from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Set path to GeckoDriver executable
driver_path = "/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver"
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--start-maximized")

# Initialize the Firefox browser
driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)

try:
    URL = "http://localhost:5000/easytesting"
    driver.get(URL)
    driver.maximize_window()
    time.sleep(5)

    element = driver.find_element(By.ID, "menu")
    time.sleep(2)
    actions = ActionChains(driver)
    actions.context_click(element).perform()

    print("Test Case Failed : ")

except Exception as e:
    print("Test Case Failed : ")
