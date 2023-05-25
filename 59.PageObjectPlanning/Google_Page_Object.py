from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class GooglePageObject:
    def __init__(self, driver):
        self.driver = driver

        # Keep on locating objects here
        self.textbox = (By.NAME, "a")
        self.button = (By.CLASS_NAME, "gNO89b")

    # Actions on those objects
    def enter_text_in_textbox(self, text):
        self.driver.find_element(*self.textbox).send_keys(text)

    def click_search_button(self):
        self.driver.find_element(*self.button).send_keys(Keys.RETURN)
