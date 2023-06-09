from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# Set the path to the geckodriver executable
geckodriver_path = "/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver"

# Set Firefox options
options = Options()
options.headless = True

# Create a Firefox webdriver instance
driver = webdriver.Firefox(executable_path=geckodriver_path, options=options)

# Open the login page
driver.get("https://the-internet.herokuapp.com/login")

# Enter username and password
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# Click the login button
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/button/i").click()

# Create a file to store the login information
file_path = "Cookies.data"
with open(file_path, "w") as file:
    # Loop through the cookies and write them to the file
    for cookie in driver.get_cookies():
        file.write(
            f"{cookie['name']};{cookie['value']};{cookie['domain']};{cookie['path']};{cookie['expiry']};{cookie['secure']}\n"
        )

# Close the browser
driver.quit()
