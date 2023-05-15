from selenium import webdriver
import time

driver = webdriver.Remote(desired_capabilities=webdriver.DesiredCapabilities.CHROME,command_executor="http://192.168.100.37:4444/ui")

try:
    URL="https://www.google.com"
    driver.get(URL)
    driver.maximize_window()
    time.sleep(5)
    print(driver.title)

    print("Test Case Passed")

except Exception as e:
    print("Test Case Failed:")