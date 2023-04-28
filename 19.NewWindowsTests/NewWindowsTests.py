from selenium import webdriver
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome(executable_path="C://Selenium//driver//chromedriver_win32//chromedriver.exe")
URL = "http://localhost:5000/easytesting"
driver.get (URL)

try:
    driver.maximize_window()
    driver.find_element_by_id("btnk").click()
    print(driver.current_window_handle)
    # Provides all windows handle value
    handles=driver.window_handles

    for handle in handles:
        driver.switch_to.window(handle)
        # Switching to the desired window
        if (driver.title=="Hotel feedback"):

            driver.find_element_by_id("exampleFormControlInput1").send_keys("Alan_Alford63@hotmail.com")

            Rating = Select(driver.find_element_by_id('exampleFormControlSelect1'))
            # by value
            Rating.select_by_value("1")

            Problem = Select (driver.find_element_by_id('exampleFormControlSelect2'))
            # by value
            Problem.select_by_value("AC")
            Problem. select_by_value("Wifi")

            driver.find_element_by_id("exampleFormControlTextareal").send_keys("Not Satisfactory")
            print(driver.title)

except Exception as e:
    print("ERROR: ")