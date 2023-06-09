from selenium import webdriver

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)

try:
    URL = "http://localhost:5000/easytesting"
    driver.get(URL)
    driver.maximize_window()
    #Framel Operations
    driver.find_element_by_id("exampleFormControlInput1").send_keys("Alan_Alford63@hotmail.com")
    driver.find_element_by_id("exampleFormControlTextareal").send_keys("Satisfactory")

    #Frame2 Operations
    driver.switch_to.frame("frame2")

    driver.find_element_by_id("inputEmail4").send_keys("Alan_Alford63@hotmail.com")
    driver.find_element_by_id("inputPassword4").send_keys("Alan_Alford63")
    driver.find_element_by_id("inputAddress").send_keys("3077b Oak Ave")
    driver.find_element_by_id("inputAddress2").send_keys("Newton Building, Ste 472")
    driver.find_element_by_id("inputCity").send_keys("Seattle")
    driver.find_element_by_id("inputZip").send_keys ("WA 98195")

    print("Test Case Passed : ")

except Exception as e:
    print("Test Case Failed : ")