import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#initialize Chrome
driver=webdriver.Chrome(executable_path='C:/bin/chromedriver3.exe')

#Open URL
driver.get('http://automationpractice.com/index.php')
driver.maximize_window()

#Search for a keyword - ID Locator
#search=driver.find_element_by_id('search_query_top')
#search2=driver.find_element(By.ID, 'search_query_top')

#search.click()
#search.send_keys('Hello')

#Submit button - Name Locator
#submit=driver.find_element_by_name('submit_search')
#submit.click()

#Sign in - CLASS NAME Locator
#sign_in=driver.find_element_by_class_name('login')
#sign_in.click()

#CONTACT US - LINKTEXT Locator
#contact=driver.find_element_by_link_text('Contact us')
#contact.click()

#CONTACT US - PARTIAL LINKTEXT Locator
contact2= driver.find_element_by_partial_link_text('Contact')
contact2.click()