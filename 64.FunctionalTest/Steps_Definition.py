from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import unittest

from easytesting_page_object import EasyTestingPageObject


class StepDefinition(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.headless = True  # Set headless mode to True if you don't want to see the browser
        self.driver = webdriver.Firefox(options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_step_definition(self):
        self.driver.get("http://localhost:3000/login")
        self.assertEqual(self.driver.title, "Easy Testing")

        page_object = EasyTestingPageObject(self.driver)
        page_object.email("Andreib123@gmail.com")
        page_object.rating(1)
        page_object.problem_faced(4)
        page_object.feedback("Excellent")

        page_object.search_button()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
