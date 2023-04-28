from selenium import webdriver

try:
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.download.folderList", 2)
    profile.set_preference("browser.download.manager showWhenStarting", False)
    profile.set_preference("browser.download.dir", "C:/Users/HP/Desktop")
    profile.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream,application/zip")

    driver = webdriver.Firefox(executable_path="C:/Selenium/driver/chromedriver_win32/geckodriver.exe", firefox_profile=profile)
    driver.get ("https://www.selenium.dev/downloads/")
    driver.find_element_by_xpath("").click()

    print("Downloaded Successfully")

except Exception as e:
    print("Error: ")