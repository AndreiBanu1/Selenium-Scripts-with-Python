from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

class HandleSSLCertificate:
    def test_method(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_capability(DesiredCapabilities.ACCEPT_INSECURE_CERTS, True)

        driver = webdriver.Firefox(
            executable_path='/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver',
            options=firefox_options,
            desired_capabilities=DesiredCapabilities().FIREFOX
        )
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.get('https://cacert.org')
        print(driver.title)
        driver.quit()

handle_ssl_certificate = HandleSSLCertificate()
handle_ssl_certificate.test_method()
