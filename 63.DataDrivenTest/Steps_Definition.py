from selenium import webdriver
from selenium.webdriver.common.by import By

class StepDefinition:
    def __init__(self):
        self.driver = None

    def setup(self):
        print("Browser opened successfully")
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def navigation(self):
        self.driver.get("http://localhost:3000/login")
        print("Navigated to Easy Testing")

    def login_auth(self, arg1, arg2):
        email_field = self.driver.find_element(By.ID, "email")
        password_field = self.driver.find_element(By.ID, "password")
        email_field.send_keys(arg1)
        password_field.send_keys(arg2)
        print("Filled the Credentials")

    def login_button_should_exist(self):
        login_button = self.driver.find_element(By.ID, "btn")
        login_button.click()
        print("Logged in Successfully")

    def teardown(self):
        self.driver.quit()

if __name__ == "__main__":
    step_def = StepDefinition()
    step_def.setup()
    step_def.navigation()
    step_def.login_auth("Alchemytraining123@gmail.com", "password")
    step_def.login_button_should_exist()
    step_def.teardown()
