from selenium import webdriver

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()  # or use any other WebDriver

def after_scenario(context, scenario):
    context.driver.quit()
