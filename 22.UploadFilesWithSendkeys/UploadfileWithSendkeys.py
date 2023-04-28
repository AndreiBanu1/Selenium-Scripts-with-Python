from selenium import webdriver
driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)
URL = "http://localhost:5000/upload"
driver.get(URL)

try:
    driver.maximize_window()
    upload=driver.find_element_by_id("exampleFormControlfilel")
    upload.send_keys("C://Users/HP/Desktop/Alex/Alex_doc.docx")
    print ("File Uploaded Successfully")

except Exception as e:
    print("ERROR : ")