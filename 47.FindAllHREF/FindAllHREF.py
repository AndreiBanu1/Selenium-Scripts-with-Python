import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

try:
    url = 'https://www.google.com'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    elems = driver.find_elements(By.XPATH, "//a[@href]")
    for elem in elems:
        print(elem.get_attribute("href"))
    print("Test Case Passed: ")

except Exception as e:
    print("Test Case Failed: ")