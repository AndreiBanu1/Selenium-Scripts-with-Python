import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

try:
    url = 'https://www.localhost:5000/action'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    driver.execute_script('return document.getElementById("myBtn).click()')
    print("Test Case Passed: ")

except Exception as e:
    print("Test Case Failed: ")