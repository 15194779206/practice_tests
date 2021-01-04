from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://testadmin.jiajiabank.com/')
driver.dir.find_element_by_xpath('//*[@id="__layout"]/div/div/div[2]/div[1]/input').send_keys('lyang@jiajiabank.com')
driver.dir.find_element_by_xpath('//*[@id="__layout"]/div/div/div[2]/div[2]/input').send_keys('admin1234')
# 等待验证码输入
time.sleep(10)  # 等待输入验证码，此处方法没有万能码，只能手动输入
driver.dir.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/button').click()
