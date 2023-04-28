import time

from HtmlTestRunner.runner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleSearch(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(self):
        options = Options()
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.delete_all_cookies()
        self.driver.get("http://www.google.com/")

    def test_search(self):
        # accept cookies
        try:
            wait = WebDriverWait(self.driver, 10)
            self.cookies_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='tHlp8d']")))
            self.cookies_field.click()
            print("Cookies accepted")
        except:
            print("No cookies to accept")
            self.driver.close()

        # get the search textbox
        wait = WebDriverWait(self.driver, 10)
        self.search_field = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
        # enter search keyword and submit
        self.search_field.send_keys("Selenium WebDriver Interview Question")
        self.search_field.submit()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    test1 = unittest.TestLoader().loadTestsFromTestCase(GoogleSearch)
    suite = unittest.TestSuite(test1)
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    runner = HTMLTestRunner(log=True, verbosity=2,
                            output="/Reports",
                            title='Test report', report_name='google_search_report',
                            open_in_browser=True, description="HTMLTestReport", tested_by="Andrei B",
                            add_traceback=False)
    runner.run(suite)


