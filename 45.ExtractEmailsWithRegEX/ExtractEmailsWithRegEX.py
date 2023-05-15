import re
import time

from selenium import webdriver

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

try:
    url = 'https://localhost:5000/emails'
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    doc = driver.page_source
    emails = re.findall(r'[\w\.-]+@[\w\.-]',doc)
    for email in emails:
        print(email)
    print("Test Case Passed: ")

except Exception as e:
    print("Test Case Failed: ")