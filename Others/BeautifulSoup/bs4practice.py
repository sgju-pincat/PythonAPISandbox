from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('http://naver.com')

# soup = BeautifulSoup(driver.page_source)
# print(soup.select('div'))
# driver.execute_script('alert("test")')
driver.find_element_by_class_name('#NM_NEWSSTAND_HEADER > div.direct_area > a:nth-child(3)').click()
# driver.implicitly_wait(1)
# driver.find_element_by_css_selector('#id').send_keys('')
# driver.find_element_by_css_selector('#pw').send_keys('')
# driver.implicitly_wait(1)
# driver.find_element_by_css_selector('.btn_login').click()
# print('aa')



