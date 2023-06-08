from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

USERNAME = "alchemytrainingl"
AUTOMATE_KEY = "Pws3iMgtEquDxq"
URL = f"https://{USERNAME}:{AUTOMATE_KEY}@hub-cloud.browserstack.com/wd/hub"

caps = DesiredCapabilities.IPHONE
caps['os_version'] = '13'
caps['device'] = 'iPhone XS'
caps['real_mobile'] = 'true'
caps['project'] = 'Verify Google search Title'
caps['build'] = 'V.O.1'
caps['name'] = 'Verify Title'
caps['browserstack.local'] = 'false'

driver = webdriver.Remote(command_executor=URL, desired_capabilities=caps)
driver.get("http://www.google.com")

element = driver.find_element(By.NAME, "a")
element.send_keys("BrowserStack")
element.submit()

actual_title = driver.title
expected_title = "BrowserStack-Google Search"
if actual_title == expected_title:
    print("Test Passed!")
else:
    print("Test Failed")

driver.quit()
