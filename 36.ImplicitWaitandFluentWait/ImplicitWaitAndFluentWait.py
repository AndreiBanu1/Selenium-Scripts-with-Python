from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from datetime import datetime

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
url = 'https://covid-19-dc.herokuapp.com/'

driver = webdriver.Firefox(executable_path=driver_path)
driver.get(url)
driver.maximize_window()

# Implicit wait
driver.implicitly_wait(10)

# Click on an element
try:
    driver.find_element(By.XPATH, "//[@id=""]")
except NoSuchElementException:
    print('Element not found')
else:
    driver.find_element(By.XPATH, "//[@id=""]")
    print('Element found and clicked')

# Fluent wait
wait = WebDriverWait(driver, 30, poll_frequency=0.5, ignored_exceptions=[NoSuchElementException])

click_map = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=""]")))
click_map.click()

driver.quit()