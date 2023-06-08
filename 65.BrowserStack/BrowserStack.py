from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

USERNAME = "alchemytrainingl"
AUTOMATE_KEY = "Pws3iMgtEquDxq"
URL = "https://" + USERNAME + ":" + AUTOMATE_KEY + "@hub-cloud.browserstack.com/wd/hub"

caps = DesiredCapabilities.CHROME
caps['os'] = 'Windows'
caps['os_version'] = '10'
caps['browser'] = 'Chrome'
caps['browser_version'] = '80'
caps['name'] = "alchemytraining1's First Test"

driver = webdriver.Remote(command_executor=URL, desired_capabilities=caps)
driver.get("http://www.google.com")
element = driver.find_element_by_name("q")

element.send_keys("BrowserStack")
element.submit()
print(driver.title)
driver.quit()
