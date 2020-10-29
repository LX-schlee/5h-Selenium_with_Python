import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert

'''
# Handle Notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)


driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe', chrome_options=chrome_options)
driver.get('https://www.cleartrip.com/')
driver.maximize_window()
'''

'''
# Cookie Handling
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
driver.get('https://www.edreams.com/')
driver.maximize_window()
time.sleep(3)
cookie_button=driver.find_element_by_class_name('od-cookiedsc-btn')
cookie_button.click()
'''

'''
# Alerts
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
driver.get('http://www.dummypoint.com/Windows.html')
driver.maximize_window()
alert_1=driver.find_element_by_name('alertbutton')
alert_1.click()
time.sleep(1)
alert_button=driver.switch_to.alert
print(alert_button.text)
alert_button.accept()
'''

'''
# Alert #2 (Confirm Alert)
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
driver.get('http://www.dummypoint.com/Windows.html')
driver.maximize_window()
alert_2=driver.find_element_by_name('confirmalertb')
alert_2.click()
time.sleep(1)
alert_button_2=driver.switch_to.alert
print(alert_button_2.text)
alert_button_2.dismiss()
time.sleep(2)
driver.close()
'''

'''
# Alert 3 (Promt Alert)
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
driver.get('http://www.dummypoint.com/Windows.html')
driver.maximize_window()
alert_3 = driver.find_element_by_name('promtalertb')
alert_3.click()
confirm_promt_button= Alert(driver)
time.sleep(2)
confirm_promt_button.send_keys('I_love_Selenium')
time.sleep(1)
confirm_promt_button.accept()
'''

# Handle SSL Certificates
options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')

driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe', chrome_options=options)
driver.get('https://expired.badssl.com/')
driver.maximize_window()