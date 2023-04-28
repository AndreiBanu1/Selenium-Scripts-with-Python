from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class TestParallel:
    def test_case_one(self):
        driver = None
        webdriver.gecko.driver = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('https://www.google.com')

        print(driver.title)

        print('Test Case One with Thread Id: - {}'.format(str(time.time())))

        driver.quit()

    def test_case_two(self):
        driver = None
        webdriver.gecko.driver = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('https://www.selenium.dev')

        print(driver.title)

        print('Test Case Two with Thread Id: - {}'.format(str(time.time())))

        driver.quit()

test_parallel = TestParallel()
test_parallel.test_case_one()
test_parallel.test_case_two()
