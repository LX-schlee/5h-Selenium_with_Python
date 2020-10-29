import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

'''
Requirements:
FLight from Paris (Airport: Orly) to Berlin (Airport: Schoenefeld)
Departure date: 21.12.2020
Return date : 02.04.2021
'''

# initialize Chrome
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

flight_booking = 'https://www.edreams.com/'
shopping_website = 'http://automationpractice.com/index.php'

# Open URL
driver.get(flight_booking)
driver.maximize_window()

# Cookie Handling
cookies = driver.find_element_by_xpath('//button[@class="od-cookiedsc-btn accept_button"]')
cookies.click()

# Departure City
dep_city = driver.find_element_by_xpath('//input[@placeholder="From"]')
dep_city.click()
dep_city.send_keys('Paris')
time.sleep(1)

# Departure airport selection
dep_items = driver.find_elements_by_xpath('//li[contains(@class, "odf-dropdown-item")]/div[2]/span/span[2]')
for item in dep_items:
    if item.text == 'Orly':
        item.click()
        break

# Arrival city
arr_city = driver.find_element_by_xpath('//input[@placeholder="To"]')
arr_city.click()
arr_city.send_keys('Berlin')
time.sleep(2)

# click 4 times on arrow down
'''
arr_city.send_keys(Keys.ARROW_DOWN)
arr_city.send_keys(Keys.ARROW_DOWN)
arr_city.send_keys(Keys.ENTER)
'''

count = 0
while count < 4:
    arr_city.send_keys(Keys.ARROW_DOWN)
    count = count + 1
    time.sleep(1)

arr_city.send_keys(Keys.ENTER)
time.sleep(1)

# Departure date (21.12.2020)
calendar_month_dep = driver.find_element_by_xpath('//div[@class="odf-calendar-title"]')
click_next_dep = driver.find_element_by_xpath('//span[@glyph="arrow-right"]')

while calendar_month_dep.text != "December '20":
    click_next_dep.click()
    time.sleep(1)

dep_date = driver.find_element_by_xpath(
    '//div[@class="odf-calendar-title"][contains(text(), "December")]/following-sibling::node()/div[5]/div[text()="21"]')
dep_date.click()
time.sleep(2)

# Return date 02.04.2021
calendar_month_ret = driver.find_element_by_xpath('//div[@class="odf-calendar-title"]')
click_next_ret = driver.find_element_by_xpath('//span[@glyph="arrow-right"]')
while calendar_month_ret.text != "April '21":
    click_next_ret.click()
    time.sleep(1)

ret_date = driver.find_element_by_xpath(
    '//div[@class="odf-calendar-title"][contains(text(), "April")]/following-sibling::node()/div[2]/div[5]')
ret_date.click()
time.sleep(2)

# search flights
search_flights = driver.find_element_by_xpath('//button[text()="Search Flights"]')
search_flights.click()
