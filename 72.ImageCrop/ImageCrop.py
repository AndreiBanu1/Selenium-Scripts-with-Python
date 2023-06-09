from selenium import webdriver
from PIL import Image
from io import BytesIO

driver_path = '/Users/banuandreicristian/Documents/WebDrivers/geckodriver/geckodriver'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get("https://www.google.com/")

# now that we have the preliminary stuff out of the way time to get that image :D
element = driver.find_element_by_xpath('//*[@id="hplogo"]') # find part of the page you want image of
location = element.location
size = element.size
png = driver.get_screenshot_as_png() # saves screenshot of entire page
driver.quit()

im = Image.open(BytesIO (png)) # uses PIL library to open image in memory

left = location['×']
top = location['y']
right = location['×'] + size['width']
bottom = location['y'] + size['height']

im = im.crop((left, top, right, bottom)) # defines crop points
im.save('screenshot.png') # saves new cropped image