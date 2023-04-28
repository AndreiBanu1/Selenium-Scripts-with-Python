from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('http://www.google.com')

try:
    id = driver.find_elements_by_xpath("//*[@class]")
    for value in id:
        print(value.get_attribute('class'))

except Exception as e:
    print('TestCase Failed: ')

driver.close()
