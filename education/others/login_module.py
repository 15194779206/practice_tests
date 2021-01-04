from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

url='http://admin.jiajiabank.com/'
login_text='登录'
account='admin@b.com'
pwd='123456ll'
# 定义一个函数，设置等待时间
def get_ele_times(driver, times, func):
    return WebDriverWait(driver, times).until(func)

# 模块化思想，将打开的浏览器模块化
def openBrower():
    webdriver_handle=webdriver.Chrome()
    return webdriver_handle
# 打开的链接模块化
def openUrl(handle,url):
    handle.get(url)
    handle.maximize_window()

def login_test():
    # d=webdriver.Chrome()
    d=openBrower()
    # d.get(url)
    # d.maximize_window()
    openUrl(d,url)

    # time.sleep(2)等待时间设置
    account_ele=d.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[1]/input')
    account_ele.send_keys(account)
    pwd_ele=d.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/div[2]/input')
    pwd_ele.send_keys(pwd)
    # 有等待时间的登录
    ele_login=get_ele_times(d , 10 ,\
                            lambda d: d.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/button'))
    ele_login.click();
    # 点击登录按钮
    # d.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/button').click()
    try:
        d.find_element_by_link_text('账号信息和密码错误信息不匹配')
        print("账号或密码不正确")
    except:
        print("正确")
    #  关闭浏览器
    # d.close()

if __name__=='__main__':
    login_test()