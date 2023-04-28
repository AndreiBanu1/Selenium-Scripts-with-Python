from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
url = 'http://localhost:5000/resize'

driver = webdriver.Firefox(executable_path=driver_path)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()

driver.switch_to.frame(driver.find_element(By.ID, 'frame'))
widget = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]')
act = ActionChains(driver)

# Code for resize
act.click_and_hold(widget).move_by_offset(100, 100).release().perform()

print("Resized successfully")
