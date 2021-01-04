from selenium import webdriver
import time
from pub import login


driver=webdriver.Firefox()
driver.get("https://www.imooc.com/")
time.sleep(5)

#用户名和密码提取出来
# userna="15194779206"
# passwo="131214ly"


#循环读取用户名和密码
inform=open("user_Inform","r",encoding="utf-8")
fs=inform.readlines()
for user_inform in fs:
    #用户名和密码以，为分割点，分开
    users=user_inform.split(',')[0]
    passws=user_inform.split(",")[1]
    print(users,passws)



login.login(driver,users,passws)