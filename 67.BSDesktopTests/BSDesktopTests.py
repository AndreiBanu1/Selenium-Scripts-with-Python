from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

USERNAME = "alchemytrainingl"
AUTOMATE_KEY = "Pws3iMgtEquDxq"
URL = f"https://{USERNAME}:{AUTOMATE_KEY}@hub-cloud.browserstack.com/wd/hub"

caps = DesiredCapabilities.SAFARI
caps['os'] = 'OS X'
caps['os_version'] = 'Sierra'
caps['browser'] = 'Safari'
caps['browser_version'] = '10.0'
caps['project'] = 'My_First_Test'
caps['build'] = 'v.O.1'
caps['name'] = 'Test'
caps['browserstack.local'] = 'false'
caps['browserstack.selenium_version'] = '3.5.2'

driver = webdriver.Remote(command_executor=URL, desired_capabilities=caps)
driver.get("http://www.google.com")

element = driver.find_element(By.NAME, "q")
element.send_keys("BrowserStack")
element.submit()

print(driver.title)
driver.quit()
