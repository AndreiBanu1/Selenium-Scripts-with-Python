from selenium import webdriver
from selenium.webdriver.common.by import By


driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
url = 'http://localhost:5000/easytesting'

driver = webdriver.Firefox(executable_path=driver_path)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(url)

js = driver.execute_script("return window.scrollTo(0, document.body.scrollHeight)")

js = driver.execute_script("return scroll(0, 70)")

element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]")
coordinates = element.location_once_scrolled_into_view
print("Element coordinates:", coordinates)

print("Scrolled successfully")
