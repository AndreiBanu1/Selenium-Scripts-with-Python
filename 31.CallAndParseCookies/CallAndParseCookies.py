from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

options = Options()
options.headless = False
caps = DesiredCapabilities().FIREFOX
caps["marionette"] = True
driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'

driver = webdriver.Firefox(options=options, capabilities=caps, executable_path=driver_path)
driver.maximize_window()
driver.implicitly_wait(10)

try:
    driver.get("https://www.google.com")

    #Add a few cookies
    driver.add_cookie({"name": "test1", "value": "cookie1"})
    driver.add_cookie({"name": "test2", "value": "cookie2"})

    #Get specific cookie by name
    cookie1 = driver.get_cookie("test1")

    #Get all available cookies
    cookies = driver.get_cookies()
    print(cookies)
finally:
    driver.quit()
