import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#initialize Chrome


driver=webdriver.Chrome(executable_path='C:/bin/chromedriver3.exe')

#Open URL
driver.get('http://automationpractice.com/index.php')
driver.maximize_window()

'''
Xpath basic structure

//tag[@attribute="value"]
'''

#Option 1
#cart=driver.find_element_by_xpath('//a[@title="View my shopping cart"]')
#cart.click()

#Option 2
#cart2=driver.find_element(By.XPATH, '//a[@title="View my shopping cart"]')
#cart2.click()

#Option 3- absolute X path expression
cart3=driver.find_element_by_xpath('html/body/div/div/header/div[3]/div/div/div[3]/div/a')
cart3.click()