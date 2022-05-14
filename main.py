import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")
driver.implicitly_wait(8)
my_element = driver.find_element_by_id('downloadButton')
my_element.click()

