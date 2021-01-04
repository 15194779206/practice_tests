from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

#预输入信息设置
url='https://www.imooc.com/'
login_text='登录'
user_name='15194779206'
pass_word='131214ly'

def get_ele_times(driver,times,func):
    return WebDriverWait(driver,times).until(func)

def Test():
    brower = webdriver.Firefox()
    brower.get(url)
    brower.maximize_window()
    # 等待时间
    # ele_login=get_ele_times(brower,10,lambda brower:brower.find_element_by_link_text(login_text))
    # ele_login.click()
    time.sleep(2)
    brower.find_element_by_link_text(login_text).click()
    time.sleep(2)
    user_na = brower.find_element_by_class_name("ipt-email")
    # user_na.send_keys(" ")
    user_na.clear()
    user_na.send_keys(user_name)
    pass_wo = brower.find_element_by_class_name("ipt-pwd")
    pass_wo.send_keys(pass_word)
    login=brower.find_element_by_xpath("/html/body/div[7]/div[2]/div/div/form/div[5]")
    login.click()
    try:
        brower.find_element_by_link_text("密码错误")
        print("此处输入有误")
    except:
        print("输入正确")
if __name__=='__main__':
     Test()



