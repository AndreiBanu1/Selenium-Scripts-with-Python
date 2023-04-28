from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.chrome(executable_path="C://Selenium//driver//chromedriver_win32//chromedriver.exe")
URL = "http://localhost:5000/easytesting"
driver.get (URL)

try:
    driver.maximize_window()
    driver.find_element_by_id("inputEmail4").send_keys("Alan_Alford63@hotmail.com")
    driver.find_element_by_id("inputPassword4").send_keys("Alan_Alford63")
    driver.find_element_by_id("inputAddress").send_keys("3077b Oak Ave")
    driver.find_element_by_id("inputAddress2").send_keys("Newton Building, Ste 472")
    driver.find_element_by_id("inputCity").send_keys("Seattle")
    driver.find_element_by_id("inputZip").send_keys("WA 98195")
    #opting Multi options
    opt=Select(driver.find_element_by_id('inputgadget'))
    opt.select_by_index(2)
    opt.select_by_index(1)

    driver.find_element_by_id('inputZip').send_keys("WA 98195")
    opt.deselect_by_index(2)
    opt.deselect_by_index(1)
    print("Test Case Passed : ")

except Exception as e:
    print("Test Case Failed: ")