import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# initialize chrome driver
driver=webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')

ecommerce = 'http://automationpractice.com/index.php'
uipractice = 'http://uitestpractice.com/'

driver.get(uipractice)
driver.maximize_window()

# Initialize ActionChains
actions=ActionChains(driver)

'''
# Move the mouse to a specific element
women = driver.find_element_by_xpath('//a[text()="Women"]')
blouses= driver.find_element_by_xpath('//a[text()="Blouses"]')
actions.move_to_element(women).perform()
time.sleep(2)
blouses.click()
'''

'''
# Open a page in a new Tab
sign_in=driver.find_element_by_class_name('login')
actions.key_down(Keys.CONTROL).click(sign_in).key_up(Keys.CONTROL).perform()
'''

'''
# Drag and Drop
draggable_element=driver.find_element_by_id('draggable')
droppable_element=driver.find_element_by_id('droppable')
# actions.click_and_hold(draggable_element).move_to_element(droppable_element).release().perform() #alternative 1
actions.drag_and_drop(draggable_element,droppable_element).perform() # alternative 2
'''

'''
# Double Click
button=driver.find_element_by_name('dblClick')
actions.double_click(button).perform()
'''

# Right Click
home_button=driver.find_element_by_xpath('//a[text()="Home"]')
actions.context_click(home_button).perform()