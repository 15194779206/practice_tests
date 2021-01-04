from selenium import webdriver
driver=webdriver.Firefox()
driver.get("file:///C:/Workspace-python/jiajiabank/C：zidonghua/shijian.html")
driver.find_element_by_id('time').send_keys('2019-01-16')
print(driver.find_element_by_id('time').get_attribute('value'))
