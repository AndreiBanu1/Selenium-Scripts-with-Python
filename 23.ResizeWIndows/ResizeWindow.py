from selenium import webdriver

driver=webdriver.Chrome (executable_path="C://Selenium//driver//chromedriver_win32//chromedriver. exe")

try:
    URL = "http://localhost:5000/easytesting"
    driver.get (URL)
    driver.set_window_size(600,700)
    driver.set_window_position(150,150)| driver.find_element_by_class_name("navbar-toggler-icon").click()
    print("UI is responsive, Test case Passed")

except Exception as e:
    print ("ERROR : ")
