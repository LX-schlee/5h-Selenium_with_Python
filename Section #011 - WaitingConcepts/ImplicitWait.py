import time
from selenium import webdriver


# initialize Chrome
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

flight_booking = 'https://www.edreams.com/'

# Open URL
driver.get(flight_booking)
driver.maximize_window()

help_button=driver.find_element_by_class_name('header_help')
help_button.click()

# switch to child window
child_window=driver.window_handles[1]
driver.switch_to.window(child_window)

driver.implicitly_wait(10)
refunds_button=driver.find_element_by_xpath('//a[text()="Refunds"]')
refunds_button.click()