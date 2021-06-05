from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   #判断正确与否
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

brower=webdriver.Firefox()
brower.get("http://testadmin.jiajiabank.com/")
brower.find_element_by_xpath('//*[@id="__layout"]/div/div/div[2]/div[1]/input').send_keys("lyang@jiajiabank.com")
brower.find_element_by_xpath('//*[@id="__layout"]/div/div/div[2]/div[2]/input').send_keys('admin1234')
#等待验证码输入
str1 = input("Enter your input: ")
input = brower.find_element_by_xpath('//*[@id="__layout"]/div/div/div[2]/div[3]/input')
input.send_keys(str1)
input.send_keys(Keys.ENTER)
# element=WebDriverWait(brower,10,0.5).until(
# EC.presence_of_element_located((By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div[3]/input'))
# )
brower.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/button').click()
time.sleep(4)
brower.get('http://testadmin.jiajiabank.com/admin/operatingcenter/contentManagement/addadvertising')
brower.find_element_by_xpath('/html/body/div/div[2]/div/section/section/main/div/div/div[2]/div[1]/input').send_keys('2019测试')
brower.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/main/div/div/div[2]/div[2]/div/div/input').click()
brower.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()
brower.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/main/div/div/div[2]/div[3]/div/div/input').click()
brower.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[2]').click()
#日期弹出框
ele=brower.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/main/div/div/div[2]/div[4]/div/input')
# ActionChains(brower).click(ele).perform()
# sub_text=brower.find_element_by_link_text('16')
# wait=WebDriverWait(sub_text,10)
brower.find_element_by_xpath('/html/body/div[4]/div[2]/button[1]').click()






"""
brower.get('http://testadmin.jiajiabank.com/admin/investment/managementOfMark/managedtarget')
brower.find_element_by_xpath('/html/body/div/div[2]/div/section/section/main/div/div[2]/div[1]/button').click()
brower.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/main/div/div[1]/div/div[1]/div/div/div/input').send_keys("十一月测试企业")

brower.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/main/div/div[1]/div/div[2]/div/p/input').send_keys("50000")
#归属项目是下拉框

  #定位到该下拉框
#selector=Select(brower.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div[1]/div/div[4]/div/div/div[1]'))
  #通过select对象进行调用select_by_index和select_by_value坏人select_by_visiabl_text
# selector.select_by_index(2) #此处的index是从0开始的
#selector.select_by_visible_text("添加此项目不允许修改")

time.sleep(1)
select1=brower.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div[1]/div/div[4]/div/div/div/input').click()
brower.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[13]').click()
#借款期限
brower.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/main/div/div[1]/div/div[5]/div/p/input').send_keys("3")
#风险等级是下拉框
brower.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div[1]/div/div[6]/div/div/div[1]/input').click()
brower.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()

#项目名称
brower.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/main/div/div[1]/div/div[7]/div/p/input').send_keys("测试测试标的")
#收益率
brower.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/main/div/div[1]/div/div[8]/div/p/input').send_keys("7")
#用户起投金额
brower.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/main/div/div[1]/div/div[11]/div/p/input').send_keys("1000")
#开始募集时间
brower.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div[1]/div/div[10]/div/div/input').send_keys('2019-01-25')



#结束募集时间
brower.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div[1]/div/div[13]/div/div/input').click()
time.sleep(1)
brower.find_element_by_xpath('/html/body/div[5]/div[1]/div/div[3]/table[1]/tbody/tr[3]/td[6]/div/span').click()
brower.find_element_by_xpath('/html/body/div[4]/div[2]/button[2]').click()

#付息方式
brower.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div[1]/div/div[14]/div/div/div/input').click()
brower.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()

#企业描述
brower.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div[2]/div/div[1]/textarea').send_keys("添加的内容描述")
#资料信息
brower.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div[2]/div/div[2]/div/div/button').click()

"""