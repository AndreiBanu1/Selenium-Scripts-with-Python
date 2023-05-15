from selenium import webdriver

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get("http://localhost:5000/easytesting")

if driver.find_element_by_id("exampleInputEmaill").is_displayed():
    print("Email Text field is Visible")
else:
    print("Email Text field is Not Visible")

if driver.find_element_by_id("rec").is_enabled():
    print("Receive News Letter radio button is Selected.")
else:
    print("Receive News letter radio button is Not Selected.")

driver.quit()