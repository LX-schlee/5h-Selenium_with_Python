import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

wait=WebDriverWait(driver, 10)
refunds_button=wait.until(EC.element_to_be_clickable((By.XPATH,'//a[text()="Refunds"]' )))
refunds_button.click()