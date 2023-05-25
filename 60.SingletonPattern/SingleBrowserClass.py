from selenium import webdriver

class SingletonBrowserClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._initialize_driver()
        return cls._instance

    def _initialize_driver(self):
        driver_path = "/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver"
        self.driver = webdriver.Firefox(executable_path=driver_path)

    @staticmethod
    def get_instance_of_singleton_browser_class():
        return SingletonBrowserClass()

    def get_driver(self):
        return self.driver
