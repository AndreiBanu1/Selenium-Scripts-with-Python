import logging
from selenium import webdriver

LOG_FILENAME = 'Google Search Log.out'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

logging.debug('Chrome Instance Started and working fine')
driver.get('http://www.google.com')
logging.debug('Navigated to Google webpage')

driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div[1]/a").is_displayed()
logging.debug ('Gmail link is available')

driver.find_element_by_xpath('/htm1/body/div[1]/div[1]/div/div/div/div[1]/div[2]/a').is_displayed()
logging. debug ('Image link is available')

driver.find_element_by_xpath('/html/body/div[1]/div[2]/form/div[2]/div[1]/div[1]/div/div[2]/input').send_keys("Selenium Testing")
logging. debug ('Typed in Search Textfield')

driver.find_element_by_xpath('/htm1/body/div[1]/div[2]/form/div[2]/div[1]/div[3]/center/input[1]').click()
logging.debug('Clicked on search Button')