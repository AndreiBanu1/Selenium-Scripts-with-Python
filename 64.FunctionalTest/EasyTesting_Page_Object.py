from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class EasyTestingPageObject:
    def __init__(self, driver):
        self.driver = driver

    def feedback(self, text):
        textbox = self.driver.find_element(By.ID, "exampleFormControlTextarea1")
        textbox.send_keys(text)

    def rating(self, i):
        rating_dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect1"))
        rating_dropdown.select_by_index(i)

    def problem_faced(self, i):
        service_dropdown = Select(self.driver.find_element(By.ID, "exampleFormControlSelect2"))
        service_dropdown.select_by_index(i)

    def email(self, text):
        email_field = self.driver.find_element(By.ID, "exmapleFormControlInput1")
        email_field.send_keys(text)

    def search_button(self):
        button = self.driver.find_element(By.ID, "btn")
        button.send_keys(Keys.RETURN)
