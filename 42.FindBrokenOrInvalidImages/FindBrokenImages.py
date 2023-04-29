import urllib.request
from urllib.error import HTTPError
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:5000/images")
driver.maximize_window()

elements = driver.find_elements_by_tag_name("img")
print(f"Total number of Images on webpage: ----››{len(elements)}")

for ele in elements:
    try:
        conn = urllib.request.urlopen(ele.get_attribute("src"))
        if conn.status != 200:
            print("Broken Image:---->>" + ele.get_attribute("src"))
        else:
            print("Fine Image:------->" + ele.get_attribute("src"))
    except HTTPError:
        print("Broken Image:---->>" + ele.get_attribute("src"))

driver.close()
