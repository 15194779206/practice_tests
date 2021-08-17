from selenium import webdriver
import unittest
import time
import random
from selenium.webdriver.common.action_chains import ActionChains
import pymysql

class liginTest(unittest.TestCase):
    def setUp(self):
        self.dir=webdriver.Firefox()
        self.path='http://testwww.jiajiabank.com/login'
        self.user_name='14400000050'
        self.Passw='admin1234'
        self.conn = pymysql.connect('localhost', 'root', '123456', 'shuju1')

    # 登录因为每个测试方法都需要进行调用
    def Login(self):
        self.dir.get(self.path)
        self.dir.find_element_by_class_name('login-user').send_keys(self.user_name)
        self.dir.find_element_by_class_name('login-pwd').send_keys(self.Passw)
        self.dir.find_element_by_class_name('login-btndia').click()
        time.sleep(2)

    def  testCha(self):
        self.Login()
        self.dir.get('http://testwww.jiajiabank.com/myaccount/moneywater')
        self.dir.find_element_by_xpath('//*[@id="__layout"]/div/div/div[3]/div[2]/ul/li[1]/div/div').click()
        self.dir.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/table/tbody/tr[4]/td[4]').click()
        self.dir.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/table/tbody/tr[6]/td[5]').click()

    def testMysql(self):

        get_cursor=self.conn.cursor()
        sql='select * from loginTest '
        #查询
        get_cursor.execute(sql)
        print(get_cursor.execute(sql))
        #获取所有的数据表
        res=get_cursor.fetchall()
        for i in res:
            print(i)

    #关闭操作
    def tearDown(self):
        self.conn.close()



if __name__ =='__main__':
    unittest.main()




