import time
from selenium import webdriver
import logging

# logging configurations
logging.basicConfig(filename='logs_example.log', format= '%(asctime)s: %(levelname)s: %(message)s', datefmt='%y/%m/%d %H:%M:%S', level=logging.INFO, filemode='w')

# initialize Chrome
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

shopping_website = 'http://automationpractice.com/index.php'

# Open URL
driver.get(shopping_website)
driver.maximize_window()
time.sleep(1)
logging.info('Website was opened and the window was maximized')


# Example 1- Scroll into view
about_us=driver.find_element_by_xpath('//a[contains(text(),"About")]') # element no.1
about_us.location_once_scrolled_into_view
time.sleep(1)
about_us.click() # click on element no.1
logging.info('About us button was clicked')

time.sleep(2)
driver.back() # go back
time.sleep(1)

contact_us = driver.find_element_by_xpath('//a[text()="Contact us"]') # element no.2
contact_us.location_once_scrolled_into_view
time.sleep(1)
contact_us.click()
logging.info('Contact us button was clicked successfully')

driver.close() # close driver
logging.info('Driver closed successfully')