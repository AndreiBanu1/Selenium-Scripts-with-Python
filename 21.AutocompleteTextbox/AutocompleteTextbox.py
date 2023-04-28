from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)
URL = "http://localhost:5000/easytesting"
driver.get(URL)

try:
    driver.maximize_window()
    Suggestion_box=driver.find_element_by_id("myInput")
    Suggestion_box.send_keys("In")
    Suggestion_box.send_keys (Keys.ARROW_DOWN)
    Suggestion_box.send_keys (Keys.RETURN)
    print("Tested Autocomplete")

except Exception as e:
    print("ERROR : ")