from selenium import webdriver
import time

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

try:
    URL = "http://www.google.com"
    driver.get (URL)
    driver.maximize_window()
    time.sleep (5)
    Class_elems = driver.find_elements_by_xpath('//*[@class]')
    for elem in Class_elems:
        print(elem.get_attribute ('class'))
    print("Test Case Passed : ")

except Exception as e:
    print ("Test Case Failed : ")