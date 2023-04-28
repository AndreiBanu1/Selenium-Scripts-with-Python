from selenium import webdriver
driver=webdriver.Chrome(executable_path="C://Selenium//driver//chromedriver_win32//chromedriver.exe")
URL = "http://localhost:5000/easytesting"

driver.get (URL)
driver.maximize_window()

driver.find_element_by_id("exampleInputEmaill").send_keys("Alan Alford63@hotmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Alan Alford63")

# Handling Multiple checkbox
driver.find_element_by_id("privacypolicy").click()
driver.find_element_by_id("TNC").click()
driver.implicitly_wait(10)

# To verify or get selection status
isChecked = driver.find_element_by_id("privacypolicy").get_attribute("checked")

if isChecked is not None:
    print('Element checked - ', isChecked)
else:
    print("Element checked - false")