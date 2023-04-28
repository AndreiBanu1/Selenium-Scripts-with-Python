from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

driver_path = "/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver"
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

driver.maximize_window()
#username and password
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
Msg = driver.find_element(By.CSS_SELECTOR, "p").text
print(Msg)

driver.close()
