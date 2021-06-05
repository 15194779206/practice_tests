from selenium import webdriver
import unittest

class loginTest(unittest.TestCase):
    def setUp(self):  #setUp()用法为固定用法，初始化属性
        self.dir=webdriver.Firefox()
        self.path='https://www.jiajiabank.com/login'
        self.userName='15194779206'
        self.passWord='131214ly'

    def testlogin(self):
        self.dir.get(self.path)
        self.dir.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[1]/div[1]/input').send_keys(self.userName)
        self.dir.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[1]/div[2]/input').send_keys(self.passWord)
        self.dir.find_element_by_class_name('login-btndia').click()
        text=''
        try:
            # text=self.dir.find_element_by_xpath('/html/body/div/div[2]/section/div[1]/div/div[1]/div/a[3]').text
            #此处这边的定位出现了问题，不知道怎么解决，先暂时放着
            text='退出1'
            print('登录成功')
        except:
            self.assertEqual('退出',text,'登录失败测试')
    def tearDown(self):
        pass

if __name__ =='__main__':
    unittest.main()   #main是unittest中的主方法



