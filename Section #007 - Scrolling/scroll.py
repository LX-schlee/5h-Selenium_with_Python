import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# initialize Chrome
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

flight_booking = 'https://www.edreams.com/'
shopping_website = 'http://automationpractice.com/index.php'

# Open URL
driver.get(shopping_website)
driver.maximize_window()
time.sleep(1)

'''
# Example 1- Scroll into view
about_us=driver.find_element_by_xpath('//a[contains(text(),"About")]') # element no.1
about_us.location_once_scrolled_into_view
time.sleep(1)
about_us.click() # click on element no.1

time.sleep(2)
driver.back() # go back
time.sleep(1)

contact_us = driver.find_element_by_xpath('//a[text()="Contact us"]') # element no.2
contact_us.location_once_scrolled_into_view
time.sleep(1)
contact_us.click()

driver.close() # close driver
'''

'''
# Example 2 - Keys Class
about_us=driver.find_element_by_xpath('//a[contains(text(),"About")]') # element no.1
about_us.send_keys(Keys.PAGE_DOWN)
time.sleep(3)
about_us.click() # click on element no.1
time.sleep(2)
driver.back() # go back
time.sleep(2)
contact_us = driver.find_element_by_xpath('//a[text()="Contact us"]') # element no.2
contact_us.send_keys(Keys.PAGE_UP)
time.sleep(3)
contact_us.click() # click on element no.2
time.sleep(1)
driver.close() # close driver
'''

# Example 3- ActionChains
about_us=driver.find_element_by_xpath('//a[contains(text(),"About")]') # element no.1
actions_1= ActionChains(driver)
actions_1.move_to_element(about_us).perform() #move to element no. 1
time.sleep(2)
about_us.click() # click on element no.1
time.sleep(2)
driver.back()
time.sleep(1)
actions_2=ActionChains(driver)
contact_us = driver.find_element_by_xpath('//a[text()="Contact us"]') # element no.2
actions_2.move_to_element(contact_us).perform() #move to element no. 2
time.sleep(2)
contact_us.click() #click on element no.2
time.sleep(2)
driver.close() # close driver