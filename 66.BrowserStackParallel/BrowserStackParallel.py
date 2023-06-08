import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

USERNAME = "alchemytrainingl"
AUTOMATE_KEY = "Pws3iMgtEquDxq"
URL = f"https://{USERNAME}:{AUTOMATE_KEY}@hub-cloud.browserstack.com/wd/hub"

class BrowserStack(unittest.TestCase):
    def setUp(self):
        self.driver = None

    def tearDown(self):
        if self.driver is not None:
            self.driver.quit()

    def test_executeSessionOne(self):
        caps = DesiredCapabilities.CHROME
        caps['os'] = 'Windows'
        caps['os_version'] = '10'
        caps['browser'] = 'Chrome'
        caps['browser_version'] = '80'
        caps['name'] = "alchemytraining1's First Test"

        self.driver = webdriver.Remote(command_executor=URL, desired_capabilities=caps)
        self.driver.get("http://www.google.com")
        time.sleep(3)  # Wait for 3 seconds
        self.driver.quit()

    def test_executeSessionTwo(self):
        caps = DesiredCapabilities.CHROME
        caps['os_version'] = '11'
        caps['device'] = 'iPhone 8 Plus'
        caps['real_mobile'] = 'true'
        caps['browserstack.local'] = 'false'

        self.driver = webdriver.Remote(command_executor=URL, desired_capabilities=caps)
        self.driver.get("https://login.yahoo.com/")
        time.sleep(3)  # Wait for 3 seconds
        self.driver.quit()

    def test_executeSessionThree(self):
        caps = DesiredCapabilities.CHROME
        caps['os'] = 'OS X'
        caps['os_version'] = 'Catalina'
        caps['browser'] = 'Chrome'
        caps['browser_version'] = '83.0'
        caps['browserstack.local'] = 'false'
        caps['browserstack.selenium_version'] = '3.5.2'

        self.driver = webdriver.Remote(command_executor=URL, desired_capabilities=caps)
        self.driver.get("https://www.browserstack.com/")
        time.sleep(3)  # Wait for 3 seconds
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
