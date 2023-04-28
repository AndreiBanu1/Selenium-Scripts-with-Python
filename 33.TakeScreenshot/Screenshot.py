from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# Set path to GeckoDriver executable
driver_path = "/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver"
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--start-maximized")

# Initialize the Firefox browser
driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)

try:
    URL = "http://localhost:3000/"
    driver.get(URL)
    driver.maximize_window()
    time.sleep(5)

    driver.save_screenshot("Landing_Page.png")

    driver.find_element(By.XPATH, "/html/body/div[1]/nav/div[2]/div[2]/ul/li[2]/a").click()
    time.sleep(5)
    driver.save_screenshot("Login_Page.png")
    driver.find_element(By.ID, "email").send_keys("Alchemytraining123@gmail.com")
    driver.find_element(By.ID, "password").send_keys("P@ssword@123")
    driver.find_element(By.ID, "btn").click()
    time.sleep(5)
    driver.save_screenshot("Dashboard.png")

    print("Test Case Passed: ")

except Exception as e:
    print("Test Case Failed : ")

