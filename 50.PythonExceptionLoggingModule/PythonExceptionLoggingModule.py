import logging
from selenium import webdriver

LOG_FILENAME = 'logging_example.out'
logging.baiscConfig(filename=LOG_FILENAME, level=logging.DEBUG)

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

driver.get("http://www.google.com")

logging.debug('Firefox Instance Started and working fine')
logging.debug('Browser Version printed')