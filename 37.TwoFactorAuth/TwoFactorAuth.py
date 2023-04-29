import TOTP as TOTP
from selenium import webdriver

driver_path = 'src/test/resources/chromedriver'
url = 'http://localhost:52375/Account/Login'

driver = webdriver.Chrome(executable_path=driver_path)
driver.get(url)

driver.find_element_by_id("Input_Email").send_keys("foo@example.com")
driver.find_element_by_id("Input_Password").send_keys("P@ssw0rd")
driver.find_element_by_id("btn-login").click()

# Compute 2FA Code
otp_key_str = "6jm7n6xwitpjooh7ihewyyzeux7aqmw2" # <- this 2FA secret key.

totp = TOTP(otp_key_str)
two_factor_code = totp.now() # <- got 2FA code at this time!

driver.find_element_by_id("Input_TwoFactorCode").send_keys(two_factor_code)
driver.find_element_by_id("btn-login").click()

driver.quit()