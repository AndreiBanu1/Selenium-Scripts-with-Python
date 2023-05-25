import time
from selenium import webdriver
import pytest

from page_objects import GooglePageObject

@pytest.fixture(scope="class")
def setup(request):
    driver_path = "/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver"
    driver = webdriver.Firefox(executable_path=driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.usefixtures("setup")
class TestStepDefinitions:
    def test_open_browser(self):
        pass

    def test_navigating_to_google_page(self):
        self.driver.get("http://google.com")
        actual_title = self.driver.title
        expected_title = "Google"
        assert actual_title == expected_title

    def test_search(self):
        pom = GooglePageObject(self.driver)
        pom.enter_text_in_textbox("search_text")
        time.sleep(2)
        pom.click_search_button()
