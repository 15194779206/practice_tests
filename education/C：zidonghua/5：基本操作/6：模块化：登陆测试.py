from selenium import webdriver
import time

driver=webdriver.Firefox()
driver.get("https://www.imooc.com/")
time.sleep(2)

#用户名和密码提取出来
userna="15194779206"
passwo="131214ly"

def login(user,passw):
    driver.find_element_by_link_text("登录").click()
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/form/div[1]/input").send_keys(user)
    driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/form/div[2]/input").send_keys(passw)
    driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/form/div[5]").click()

login(userna,passwo)