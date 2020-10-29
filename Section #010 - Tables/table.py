import time
from selenium import webdriver

# tr = table row
# th = table header
# td = table data


# initialize Chrome
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
driver.get('https://www.11v11.com/league-tables/premier-league/2019/')
driver.maximize_window()

# starting point
table=driver.find_element_by_xpath('//table[@id="table-league"]')

# Print the number of rows
# rows= table.find_elements_by_xpath('.//tbody/tr')
# print(len(rows))

# Print the number of columns
# columns=table.find_elements_by_xpath('.//thead/tr/th')
# print('This is the length of the columns ' + str(len(columns)))

# Print out the whole rows
# entire_row= table.find_elements_by_xpath('.//tbody/tr')
# for row in entire_row:
#    print(row.text)
# time.sleep(1)
# driver.close()

'''
# Print out the team names
teams = table.find_elements_by_xpath('.//tbody/tr/td[2]/a')
for team in teams:
    print(team.text)
time.sleep(1)
driver.close()
'''

'''
# Print out the points
points=table.find_elements_by_xpath('.//tbody/tr/td[10]')
for point in points:
    print(point.text)
time.sleep(1)
driver.close()
'''

# Total Points
points=table.find_elements_by_xpath('.//tbody/tr/td[10]')
empty_list=[]
for point in points:
    empty_list.append(point.text)
total_points=list(map(int, empty_list))
print('The total sum is ' + str(sum(total_points)))












