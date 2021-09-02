import unittest
from selenium import webdriver
from PO.login_page import *
from lib.log import *
from conf.conf import *
from lib.readfile import *
from time import sleep


class TestKapbookLogin(unittest.TestCase):
    """Kapbook登录页面 UI自动化登录"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = test_env
        cls.driver.implicitly_wait(5)
        cls.data_list = excel_to_list(data_file, "login_page")  # 读取该测试类所有用例数据
        # self.verificationErrors = []

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # self.assertEqual([],self.verificationErrors)

    def test_1_user_tab(self):
        """账号密码登录校验"""
        sp = LoginPage(self.driver)
        sp.open(self.url)
        case_list = get_test_data(self.data_list, 'user_tab')  # 根据模块名称获取用例列表信息
        for case_data in case_list:
            if not case_data:  # 有可能为None
                print("用例数据不存在")
            case_id = case_data.get('case_id')
            case_name = case_data.get('case_name')
            username = case_data.get('username')
            pwd = case_data.get('password')
            ver_point = case_data.get('ver_point')
            # tel_num = case_data.get('tel_num')
            # ver_code = case_data.get('ver_code')
            expect_result = case_data.get('expect_result')
            sp.op_click('账号密码登录')
            sp.op_input('邮箱/手机号', username)
            sp.op_input('密码', pwd)
            sp.op_click('登录')
            # sleep(3)
            if ver_point == 'username':
                actual_result = sp.show_alert('邮箱/手机号提示')
            elif ver_point == 'password':
                actual_result = sp.show_alert('密码提示')
            try:
                self.assertEqual(expect_result, actual_result)
                log_case_info(case_id, case_name, 'PASS', {'邮箱/手机号': username, '密码': pwd},
                              expect_result, actual_result)
            except Exception as e:
                log_case_info(case_id, case_name, 'FAILED', {'邮箱/手机号': username, '密码': pwd},
                              expect_result, actual_result)


    def test_2_tel_tab(self):
        """手机验证码登录校验"""
        sp = LoginPage(self.driver)
        sp.open(self.url)
        case_list = get_test_data(self.data_list, 'tel_tab')  # 根据模块名称获取用例列表信息
        for case_data in case_list:
            if not case_data:  # 有可能为None
                print("用例数据不存在")
            case_id = case_data.get('case_id')
            case_name = case_data.get('case_name')
            # username = case_data.get('username')
            # pwd = case_data.get('password')
            ver_point = case_data.get('ver_point')
            tel_num = case_data.get('tel_num')
            ver_code = case_data.get('ver_code')
            expect_result = case_data.get('expect_result')
            sp.op_click('手机验证码登录')
            sp.op_input('手机号', tel_num)
            sp.op_input('验证码', ver_code)
            sp.op_click('登录')
            sleep(3)
            if ver_point == 'tel_num':
                actual_result = sp.show_alert('手机号提示')
            elif ver_point == 'ver_code':
                actual_result = sp.show_alert('验证码提示')
            try:
                self.assertEqual(expect_result, actual_result)
                log_case_info(case_id, case_name, 'PASS', {'手机号': tel_num, '验证码': ver_code},
                              expect_result, actual_result)
            except Exception as e:
                log_case_info(case_id, case_name, 'FAILED', {'手机号': tel_num, '验证码': ver_code},
                              expect_result, actual_result)

    def test_3_reset_pwd(self):
        """跳转忘记密码链接校验"""
        sp = LoginPage(self.driver)
        sp.open(self.url)
        sp.op_click('忘记密码')
        # self.assertEqual('请输入密码', sp.show_alert('密码'))
        # log_case_info()

    def test_4_registor(self):
        """跳转注册按钮校验"""
        sp = LoginPage(self.driver)
        sp.open(self.url)
        sp.op_click('注册')
        # self.assertEqual('请输入密码', sp.show_alert('密码'))
        # log_case_info()

    def test_5_logo_index(self):
        """跳转官网LOGO校验"""
        sp = LoginPage(self.driver)
        sp.open(self.url)
        sp.op_click('页面LOGO')
        # self.assertEqual('请输入密码', sp.show_alert('密码'))
        # log_case_info()
