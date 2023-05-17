from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class EventCapture(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigating to: ", url)

    def after_navigate_to(self, url, driver):
        print("After navigating to: ", url)

    def before_quit(self, driver):
        print("Before quitting the driver")

    def after_quit(self, driver):
        print("After quitting the driver")

    def before_navigate_back(self, driver):
        print("Before navigating back")

    def after_navigate_back(self, driver):
        print("After navigating back")

if __name__ == '__main__':
    driver = webdriver.Firefox(executable_path="/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver")

    event_handler = EventFiringWebDriver(driver, EventCapture())

    event_handler.get("https://www.google.com")
    event_handler.get("https://www.facebook.com")
    event_handler.back()
    event_handler.quit()

    print("End of Listeners Class")
