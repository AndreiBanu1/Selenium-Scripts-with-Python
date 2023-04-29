from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import unittest

class KendoUI_Date_Picker(unittest.TestCase):
    demosite = "https://demos.telerik.com/kendo-ui/datetimepicker/index"

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.demosite)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 10)

    def test_SelectDateFromKendoCalendar(self):
        # click to open the date time picker calendar.
        kendodtp = self.browser.find_element(By.CSS_SELECTOR, ".k-icon.k-i-calendar")
        kendodtp.click()

        # Provide the day of the month to select the date.
        self.HandleKendoDateTimePicker("11")

    # Function to select the day of the month in the date time picker.
    def HandleKendoDateTimePicker(self, day):
        time.sleep(5)
        table = self.browser.find_element(By.CLASS_NAME, "k-content")
        print("Kendo Calendar")
        tableRows = table.find_elements(By.XPATH, "//tr")
        for row in tableRows:
            cells = row.find_elements(By.XPATH, "td")
            for cell in cells:
                if cell.text == day:
                    cell.find_element(By.LINK_TEXT, day).click()

        time.sleep(2)

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main()
