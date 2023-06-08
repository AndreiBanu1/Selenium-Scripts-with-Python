from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

USERNAME = "alchemytrainingl"
AUTOMATE_KEY = "Pws3iMgtEquDxq"
URL = f"https://{USERNAME}:{AUTOMATE_KEY}@hub-cloud.browserstack.com/wd/hub"

caps = DesiredCapabilities.CHROME.copy()
caps['acceptInsecureCerts'] = True
caps['os'] = 'OS X'
caps['os_version'] = 'Catalina'
caps['browser'] = 'Chrome'
caps['browser_version'] = '83.0'
caps['project'] = 'SSL_Certificate'
caps['build_version_certificate'] = 'SSL V.0.1'
caps['name'] = 'SSL_bypass'
caps['browserstack.local'] = False
caps['browserstack.selenium_version'] = '3.5.2'

driver = webdriver.Remote(URL, desired_capabilities=caps)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.cacert.org")

print(driver.title)
driver.quit()
