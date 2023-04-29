from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class CalendarDatePicker(unittest.TestCase):
    def setUp(self):
        self.demosite = "http://jqueryui.com/resources/demos/datepicker"
        self.browser = webdriver.Firefox()
        self.wait = WebDriverWait(self.browser, 10)
        self.browser.maximize_window()

    def test_jquery_calendar_multiple_months(self):
        # Click to open the date time picker calendar.
        self.browser.get(self.demosite)
        cal_element = self.browser.find_element(By.ID, "datepicker")
        cal_element.click()

        # Provide the day of the month to select the date.
        self.select_day_from_multiple_date_calendar("17")

    # Function to select the day of month in the date picker.
    def select_day_from_multiple_date_calendar(self, day):
        # We are using a special XPath style to select the day of current month.
        # It will ignore the previous or next month day and pick the correct one.
        calendar_xpath = f"//td[not(contains(@class, 'ui-datepicker-other-month')) and text()='{day}']"
        calendar_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, calendar_xpath)))
        calendar_element.click()

        time.sleep(2)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()
