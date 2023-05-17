import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

class HardAssertion:
    @pytest.fixture(autouse=True)
    def setup(self):
        options = Options()
        options.add_argument("--headless")  # Uncomment this line to run the browser in headless mode
        service = Service(ChromeDriverManager().install(), chrome_type=ChromeType.GOOGLE)
        self.driver = webdriver.Chrome(service=service, options=options)
        yield
        self.driver.quit()

    def test_verifyTitle(self):
        self.driver.get("https://www.google.com")
        actual_title = self.driver.title
        expected_title = "Welcome to Google"
        assert actual_title == expected_title, "Title mismatch"
        print("This statement will not be printed")
