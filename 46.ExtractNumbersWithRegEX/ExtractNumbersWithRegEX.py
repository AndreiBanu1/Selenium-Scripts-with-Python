import re
import time

from selenium import webdriver

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

try:
    url = 'https://localhost:5000/phone-numbers'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    doc = driver.page_source
    Phone_Numbers = re.findal1(r"[(][\d]{3)[)][\s][\d]{3}-[\d]{4}", doc)
    for phone_number in Phone_Numbers:
        print(phone_number)
    print("Test Case Passed: ")

except Exception as e:
    print("Test Case Failed: ")