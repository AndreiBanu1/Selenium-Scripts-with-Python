from selenium import webdriver
driver=webdriver.Chrome(executable_path="C://Selenium//driver//chromedriver_win32//chromedriver.exe")

URL = "http://localhost:5000/easytesting"
driver.get (URL)

try:
    driver.maximize_window()
    driver.find_element_by_id("btnk").click()
    # Provides all windows handle value
    handles=driver.window_handles
    for handle in handles:
        driver.switch_to.window(handle)
        print (handle)
        # Switching to the desired window
        if(driver.title == "Advertisement"):
            print("Advertisement Window Closed")
            driver.close()
except Exception as e:
    print("Test Case Failed: ")