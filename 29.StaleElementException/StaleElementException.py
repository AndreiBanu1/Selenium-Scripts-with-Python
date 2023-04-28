from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
url = 'http://localhost:5000/stale'

driver = webdriver.Firefox(executable_path=driver_path)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()

usernameElement = driver.find_element(By.ID, "idUsername")
passwordElement = driver.find_element(By.ID, "idPassword")

usernameElement.send_keys("testuser")

driver.find_element(By.ID, "reloadLink").click()

try:
    passwordElement.send_keys("password")
except StaleElementReferenceException as Exception:
    print('Trying to find element again: - Test case Passed')
    passwordElement = driver.find_element(By.ID, "idPassword")
    passwordElement.send_keys("password")

driver.quit()