import os
from selenium import webdriver

os.environ['PATH'] += r"C:/Users/Ethan/Documents/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
