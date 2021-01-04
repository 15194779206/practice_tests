from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#基本层，创建完毕后不会修改
class Base(object):
    def __init__(self,driver,base_url='https://www.126.com/'):
        self.driver=driver
        self.base_url=base_url
        self.timeout=30
    def _open(self,url):
        urls=self.base_url+url
        print(urls)
        self.driver.get(urls)
        assert self.on_page(),"Did nnot land on %s" %url

    def on_page(self):
        return self.driver.current_url  ==(self.base_url+self.url)

    def open(self):
        self._open(self.url)

    def find_element(self,*loc): #接收元素对象
        return self.driver.find_element(*loc)

    def iframe(self,if_id):
        return self.driver.switch_to_frame(if_id)

    def script(self,src):
        return self.driver.excute_script(src)

#页面对象PO,页面层,可以创建多个页面层，进行元素定位操作
class Login(Base):
    url ='/'  #定义二级域名
    login_iframe = (By.TAG_NAME,'iframe')
    login_username_text=(By.NAME,"email")
    login_password_text=(By.NAME,"password")
    login_button=(By.ID,"dologin")
    login_user_text=(By.ID,"spbUid")

    def login_iframe(self): #做登录的方法
        self.iframe(self.login_iframe)

    def login_username(self,text):
        self.find_element(*self.login_username_text).send_keys(text)

    def login_password(self,text):
        self.find_element(*self.login_password_text).send_keys(text)

    def login_user_text(self): #获取登录之后的页面信息
        return self.find_element(*self.login_user_text).text
#测试用例层
def test_case():
    if __name__ == '__main__':
        #用例1，如果需要用例2把，下面的部分进行粘贴复制即可
        usernames='l111'
        passwords='131222y'
        driver=webdriver.Firefox()
        po=Login(driver) #调用对象
        po.open() #打开浏览器
        po.login_iframe()  #切换表单
        po.login_username(usernames)
        po.login_password(passwords)
        po.login_button()
        username = po.login_user_text()  #登录成功的页面信息
        assert username == usernames+"@126.com"  #断言信息，判断用户是否登陆成功，信息是否对应
test_case()
















