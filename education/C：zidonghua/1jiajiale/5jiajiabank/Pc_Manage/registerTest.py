from selenium import webdriver
import unittest
import pymysql
import time
import os
import sys

class registerTest(unittest.TestCase):
    def setUp(self): #setUp() 用法为固定用法，初始化属性
        self.dir=webdriver.Firefox()
        # self.path='http://testwww.jiajiabank.com/signin'
        self.pathLogin='http://testwww.jiajiabank.com/login'

    def testlogin(self):
        time.sleep(2)
        self.dir.get(self.pathLogin)
        self.dir.maximize_window()
        loginname=self.dir.find_element_by_class_name('login-user')
        loginpass=self.dir.find_element_by_class_name('login-pwd')
        infos=self.testmysql()  #获取testmysql中返回的数据信息
        lg=infos[0][1]
        ps=infos[0][2]
        loginname=loginname.send_keys(lg)
        loginpass=loginpass.send_keys(ps)
        self.dir.find_element_by_class_name('login-btn').click()
        for info in range(len(infos)):
            print(infos[info][info])
        # for info in infos:
            # loginname.clear()
            # loginname.send_keys(info[0][1])
            # time.sleep(2)
            # loginpass.clear()
            # loginpass.send_keys(info[2])




    def testmysql(self):   #注册
        # 数据库相关操作
        conn = pymysql.connect('localhost', 'root', '123456', 'shuju1')
        cursor = conn.cursor()  # 获取游标
        try:
            cursor.execute('select * from logintest')  # 数据库执行语句
            results = cursor.fetchall()    #接收全部的返回结果行
            # print(results)
            return results
            """
            for row in results:   #循环读取数据
                id = row[0]
                username = row[1]
                password = row[2]
                userinfo='''
                fid:%s,
                fuser:%s,
                fpass:%s
                '''% (id, username, password)
                # print(userinfo)
                """

        except:
            print("Error:数据库操作有误")
        conn.commit()
        conn.close()

    def testregister(self):
        time.sleep(2)
        self.dir.get(self.path)
        username=self.dir.find_element_by_class_name('signIn-user')
        password=self.dir.find_element_by_class_name('signIn-pwd')
        singin_po=self.dir.find_element_by_class_name('signIn-people')
        click_code=self.dir.find_element_by_class_name('notecode').click()




if  __name__=='__main__':
    unittest.main()





























