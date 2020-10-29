import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#initialize Chrome
driver=webdriver.Chrome(executable_path='C:/bin/chromedriver3.exe')

#Open URL
driver.get('http://automationpractice.com/index.php')
driver.maximize_window()
time.sleep(4)


'''
CSS basic syntax/structure
tag[attribute="value"]

'''

#cart1=driver.find_element_by_css_selector('a[title="View my shopping cart"]')
#cart1.click()

#logo=driver.find_element_by_css_selector('#header_logo')
#logo.click()

sign_in=driver.find_element_by_css_selector('.login')
sign_in.click()