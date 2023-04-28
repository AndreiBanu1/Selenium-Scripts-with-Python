from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#username and password in the URL
driver.get ("https://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.manage().window().maximize();