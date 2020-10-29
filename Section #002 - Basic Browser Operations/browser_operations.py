import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options=Options()
chrome_options.add_argument('--headless')

#initialize Firefox
#driver=webdriver.Firefox(executable_path='C:/bin/geckodriver.exe')

#initialize Chrome
driver2=webdriver.Chrome(executable_path='C:/bin/chromedriver3.exe', options=chrome_options)


#Open URL
driver2.get('http://automationpractice.com/index.php')
driver2.maximize_window()

#contact us button
contact=driver2.find_element_by_xpath('//a[text()="Contact us"]')
contact.click()
time.sleep(2)

#go back
driver2.back()
time.sleep(2)

#go forward
driver2.forward()
time.sleep(2)

#print the title
print('The current page title is: ' + driver2.title)
time.sleep(2)

#minimize window
driver2.minimize_window()
time.sleep(2)

#maximize window
driver2.maximize_window()
time.sleep(2)

#print URL
print('The current URL is: ' + driver2.current_url)

#refresh the website
driver2.refresh()
time.sleep(2)

#close the page
driver2.close()
print('The page was closed successfully')