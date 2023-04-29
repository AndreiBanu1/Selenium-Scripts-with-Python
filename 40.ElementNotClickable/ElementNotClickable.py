from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

service = Service('/path/to/chromedriver')  # Update the path to your chromedriver
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://login.yahoo.com")
# driver.find_element(By.ID, "persistent").click()

act = ActionChains(driver)
act.move_to_element(driver.find_element(By.ID, "persisent")).click().perform()
print("Test Case Passed")

driver.quit()
