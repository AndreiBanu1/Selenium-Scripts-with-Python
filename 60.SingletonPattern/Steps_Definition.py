from behave import given
from selenium import webdriver
from SingleBrowserClass import SingletonBrowserClass

@given("User has opened the browser")
def open_the_browser(context):
    sbc1 = SingletonBrowserClass.get_instance_of_singleton_browser_class()
    context.driver = sbc1.get_driver()
    context.driver.get("https://login.yahoo.com")

    sbc2 = SingletonBrowserClass.get_instance_of_singleton_browser_class()
    context.driver = sbc2.get_driver()
    context.driver.get("https://www.google.com")
