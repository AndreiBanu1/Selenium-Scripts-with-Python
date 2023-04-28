from selenium import webdriver
import time

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://localhost:5000/easytesting")

parent_window = driver.current_window_handle
driver.find_element_by_id("btnk").click()

for handle in driver.window_handles:
    if handle != parent_window:
        driver.switch_to.window(handle)
        time.sleep(1)
        print("Title of the new window: ", driver.title)
        print("Switching to main window...")
driver.switch_to.window(parent_window)