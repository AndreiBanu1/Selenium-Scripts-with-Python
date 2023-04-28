from selenium import webdriver

driver=webdriver.Chrome(executable_path="C://Selenium//driver//chromedriver_win32//chromedriver.exe")

try:
    URL = "http://localhost:5000/easytesting"
    driver.get (URL)
    driver.maximize_window()

    #Framel Operations
    driver.find_element_by_id("exampleInputEmaill").send_keys("Alan_Alford63@hotmail.com")
    driver.find_element_by_id("exampleInputPassword1").send_keys ("Alan Alford63")

    #Frame2 Operations
    driver.switch_frame("frame2")

    driver.find_element_by_id("inputEmail4").send_keys("Alan_Alford63@hotmail.com")
    driver.find_element_by_id("inputPassword4").send_keys("Alan_Alford63")
    driver.find_element_by_id("inputAddress").send_keys("3077b Oak Ave")
    driver.find_element_by_id("inputAddress2").send_keys("Newton Building, Ste 472")
    driver.find_element_by_id("inputCity").send_keys("Seattle")
    driver.find_element_by_id("inputZip").send_keys("WA 98195")
    print ("Test Case Passed : ")

except Exception as e:
    print("Test Case Failed : ")