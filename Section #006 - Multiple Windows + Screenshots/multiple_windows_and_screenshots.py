import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# initialize Chrome
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

flight_booking = 'https://www.edreams.com/'
shopping_website = 'http://automationpractice.com/index.php'

# Open URL
driver.get(flight_booking)
driver.maximize_window()

# Click on Help
help_ = driver.find_element_by_xpath('//a[text()="Can we help? "]')
help_.click()
time.sleep(1)

# Switch windows
child_window=driver.window_handles[1]
driver.switch_to.window(child_window)

# Click on Refunds (Child Window)
refunds = driver.find_element_by_xpath('//a[text()="Refunds"]')
refunds.click()
time.sleep(2)

# capture first screenshot
driver.save_screenshot('refunds.png')
time.sleep(1)

# Switch window to Parent window
parent_window=driver.window_handles[0]
driver.switch_to.window(parent_window)
time.sleep(1)

# Click on Manage Booking (Parent window)
manage_booking=driver.find_element_by_xpath('//button[text()="Manage booking "]')
manage_booking.click()
time.sleep(2)

# Screenshot no.2
driver.save_screenshot('screenshot #2.png')
time.sleep(1)

# Close driver
driver.quit()


