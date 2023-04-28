from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome(executable_path="C://Selenium//driver//chromedriver_win32//chromedriver.exe")
URL = "http://localhost:5000/easytesting"
driver.get(URL)

try:
    driver.maximize_window()
    driver.find_element_by_id("exampleFormControlInputl").send_keys("Alan_Alford63@hotmail.com")
    Rating=Select(driver.find_element_by_id('exampleFormControlSelect1'))

    # by value
    Rating.select_by_value ("1")
    Problem = Select(driver.find_element_by_id('exampleFormControlSelect2'))

    # by value
    Problem.select_by_value("AC")
    Problem.select_by_value( "Wifi")

    Problem.deselect_all()
    driver.find_element_by_id("exampleFormControlTextareal").send_keys("Not Satisfactory")
    print( "Test Case Passed : ")

except Exception as e:
    print( "Test Case Failed : ")