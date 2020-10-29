import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

#intialize Chrome


driver=webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

flight_booking='https://www.edreams.com/'
shopping_website='http://automationpractice.com/index.php'

#Open URL
driver.get(flight_booking)
driver.maximize_window()

'''
#Edit Box
search=driver.find_element_by_id('search_query_top')
search.click()
search.send_keys('PulloverX')
time.sleep(4)
search.send_keys(Keys.BACK_SPACE)
time.sleep(4)
search.clear()

#Button
submit=driver.find_element_by_name('submit_search')
submit.click()


#Radio Button
radio=driver.find_element_by_xpath('//div[text()="One way "]')
radio.click()

#Check Box
check_box=driver.find_element(By.XPATH, '//div[text()="Direct flights only"]')
check_box.click()

#Cookie Handling
cookies=driver.find_element_by_xpath('//button[@class="od-cookiedsc-btn accept_button"]')
cookies.click()
time.sleep(3)

#Click on link
link=driver.find_element_by_xpath('//div/span[2]/a[@href]')
link.click()
'''

# Work with static dropdowns
hotel=driver.find_element_by_xpath('//div/span[2][text()="Hotels"]')
hotel.click()
time.sleep(3)

#Work with frames
driver.switch_to.frame(0)

#select 2 rooms
rooms=driver.find_element_by_name('no_rooms')
dropdown_1=Select(rooms)
dropdown_1.select_by_index('1')
time.sleep(3)

#select 3 adults
adults=driver.find_element_by_name('group_adults')
dropdown_2=Select(adults)
dropdown_2.select_by_value('3')
time.sleep(3)

#select 4 children
children=driver.find_element_by_name('group_children')
dropdown_3=Select(children)
dropdown_3.select_by_visible_text('4')
time.sleep(3)

#switch to default content
driver.switch_to.default_content()
time.sleep(1)

#back to flight button
flights=driver.find_element_by_xpath('//div/span[2][text()="Flights"]')
flights.click()
