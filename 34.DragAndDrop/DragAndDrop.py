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
    URL = "http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"
    driver.get(URL)
    driver.maximize_window()
    time.sleep(5)

    source_element = driver.find_element_by_xpath('//*[@id="box6"')
    dest_element = driver.find_element_by_xpath('//*[@id="box106"]')
    time.sleep(2)
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, dest_element).perform()
    print("Test Case Passed : ")

except Exception as e:
    print("Test Case Failed : ")