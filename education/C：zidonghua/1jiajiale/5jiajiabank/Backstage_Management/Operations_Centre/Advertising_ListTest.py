from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC   #判断正确与否
from selenium.webdriver.common.keys import Keys
import unittest

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.dir = webdriver.Firefox()
        self.path = 'http://testadmin.jiajiabank.com/'
        self.userName = 'lyang@jiajiabank.com'
        self.passWord = 'admin1234'

    def testlogin(self):
        self.dir.get(self.path)
        self.dir.find_element_by_xpath('//*[@id="__layout"]/div/div/div[2]/div[1]/input').send_keys(self.userName)
        self.dir.find_element_by_xpath('//*[@id="__layout"]/div/div/div[2]/div[2]/input').send_keys(self.passWord)
        # 等待验证码输入
        time.sleep(10)  #等待输入验证码，此处方法没有万能码，只能手动输入
        self.dir.find_element_by_xpath('/html/body/div/div[2]/div/div/div[2]/button').click()
        """
        str1 = input("Enter your input: ")
        input = self.dir.find_element_by_xpath('//*[@id="__layout"]/div/div/div[2]/div[3]/input')
        input.send_keys(str1)
        input.send_keys(Keys.ENTER)
        """
    def testInvertest(self):  #添加广告
        self.testlogin()  #先进行登录操作
        time.sleep(2)
        self.dir.get('http://testadmin.jiajiabank.com/admin/operatingcenter/contentManagement/advertising')
        time.sleep(2)
        self.dir.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div[2]/div[1]/button').click()
        self.dir.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div/div[2]/div[1]/input').send_keys('测试添加广告列表')
        #广告位置
        self.dir.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div/div[2]/div[2]/div/div/input').click()
        self.dir.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[2]').click()
        #时间限制
        self.dir.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div/div[2]/div[3]/div/div/input').click()
        self.dir.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/ul/li[3]').click()
        #设置默认图片
        self.dir.find_element_by_xpath('/html/body/div[1]/div[2]/div/section/section/main/div/div/div[2]/div[4]/p[2]/i').click()
        #上传图片
        time.sleep(2)
        # self.dir.find_element_by_id('submit_upload').click()
        self.dir.find_element_by_xpath('//*[@id="up_file"]').send_keys(r'C:\Users\liunan\Desktop\artlogo\1.jpg')
        #上传图片
        time.sleep(2)
        ele=self.dir.find_element_by_xpath('//*[@id="__layout"]/div/section/section/main/div/div/div[2]/button')
        self.dir.execute_script('arguments[0].scrollIntoView()', ele)
        ele.click()

    def  testeditor(self):  #编辑
        pass

    def testSetDefault(self):  #设置默认
        pass
    
    def testdelete(self):  #删除
        pass


if __name__=='__main__':
    unittest.main()