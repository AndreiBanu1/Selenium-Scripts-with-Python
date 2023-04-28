from selenium import webdriver
import unittest

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class SearchText(unittest.TestCase):
    def setUp(self):
        # create a new Chrome session
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        # navigate to the application homepage
        self.driver.get("http://www.google.com/")

    def test_search_by_text(self):
        # accept cookies
        try:
            wait = WebDriverWait(self.driver, 10)
            self.cookies_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='tHlp8d']")))
            self.cookies_field.click()
            print("Cookies accepted")
        except:
            print("No cookies to accept")

        # get the search textbox
        wait = WebDriverWait(self.driver, 10)
        self.search_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='APjFqb']")))
        # enter search keyword and submit
        self.search_field.send_keys("Selenium WebDriver Interview Question")
        self.search_field.submit()

        # get the list of elements which are displayed after the search
        # currently on result page using find_elements_by_class_name method

        lists = self.driver.find_elements(By.TAG_NAME, "h3")
        no = len(lists)
        self.assertEquals(17, len(lists))

    def tearDown(self):

    # close the browser windows
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
