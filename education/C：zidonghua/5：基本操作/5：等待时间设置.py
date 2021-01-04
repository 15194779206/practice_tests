from  selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   #判断正确与否
brower=webdriver.Firefox()
brower.get("http://www.baidu.com")
#参数：驱动，时间，每多长时间访问一次
element=WebDriverWait(brower,5,0.5).until(
EC.presence_of_element_located((By.ID,"kw"))
)
element.send_keys("zhangsan")