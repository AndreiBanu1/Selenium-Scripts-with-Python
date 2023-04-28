from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C://Selenium//driver//chromedriver_win32//chromedriver.exe")
URL = "https://www.google.com/"
driver.get(URL)

try:
    driver.maximize_window()

    driver.execute_script("window.alert('This is alert');")
    time.sleep(5)
    alert=driver.switch_to.alert
    alert.accept()

    print("Dialog Box Poped-up and Successfully Handled By the script ")

except Exception as e:
    print ("ERROR : ")