from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import xmlrunner

class GenerateXMLReports(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver")

    def test_method1(self):
        self.driver.get("https://www.google.com/")
        print("Test Case 1 Passed")

    def test_method2(self):
        print(self.driver.title)
        print("Test Case 2 Passed")

    def test_method3(self):
        self.driver.find_element(By.NAME, "q").send_keys("Selenium")
        print("Test Case 3 Passed")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # Create a Test Suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GenerateXMLReports))

    # Generate TestNG XML report
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    runner.run(suite)
