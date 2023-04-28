from selenium import webdriver

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
url = 'http://www.google.com'

driver = webdriver.Firefox(executable_path=driver_path)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()


#Add cookies
driver.add_cookie({"name": "test1", "value": "cookie1"})
driver.add_cookie({"name": "test2", "value": "cookie2"})

# print all cookies
print(driver.get_cookies())

#Delete just one Cookie by name
driver.delete_cookie("test1")

#Delete all cookies
driver.delete_all_cookies()
print(driver.get_cookies())

