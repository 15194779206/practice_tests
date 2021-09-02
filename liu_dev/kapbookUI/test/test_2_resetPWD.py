import unittest
from selenium import webdriver
from PO.resetPWD_page import *
from lib.log import *
from conf.conf import *
from lib.readfile import *


class TestKapbookReset(unittest.TestCase):
    """Kapbook忘记密码页面 UI自动化登录"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.url = test_env + reset
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.data_list = excel_to_list(data_file, "resetPWD_page")  # 读取该测试类所有用例数据
        # self.verificationErrors = []

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # self.assertEqual([],self.verificationErrors)

    def test_1_resetPWD(self):
        """忘记密码校验"""
        sp = ResetPwdPage(self.driver)
        sp.open(self.url)
        case_list = get_test_data(self.data_list, 'resetPWD')  # 根据模块名称获取用例列表信息
        for case_data in case_list:
            if not case_data:  # 有可能为None
                print("用例数据不存在")
            case_id = case_data.get('case_id')
            case_name = case_data.get('case_name')
            username = case_data.get('username')
            ver_code = case_data.get('ver_code')
            new_pwd = case_data.get('newPWD')
            expect_result = case_data.get('expect_result')
            ver_point = case_data.get('ver_point')
            sp.op_input('邮箱/手机号', username)
            sp.op_input('验证码', ver_code)
            sp.op_input('新密码', new_pwd)
            sp.op_click('提交')
            if ver_point == 'username':
                actual_result = sp.show_alert('邮箱/手机号提示')
            elif ver_point == 'ver_code':
                actual_result = sp.show_alert('验证码提示')
            elif ver_point == 'new_pwd':
                actual_result = sp.show_alert('新密码提示')
            try:
                self.assertEqual(expect_result, actual_result)
                log_case_info(case_id, case_name, 'PASS', {'邮箱/手机号': username, '验证码': ver_code, '新密码': new_pwd},
                              expect_result, actual_result)
            except Exception as e:
                log_case_info(case_id, case_name, 'FAILED', {'邮箱/手机号': username, '验证码': ver_code, '新密码': new_pwd},
                              expect_result, actual_result)

    def test_2_login(self):
        """跳转登录按钮校验"""
        sp = ResetPwdPage(self.driver)
        sp.open(self.url)
        sp.op_click('登录')
        # log_case_info()

    def test_3_logo_index(self):
        """跳转官网LOGO校验"""
        sp = ResetPwdPage(self.driver)
        sp.open(self.url)
        sp.op_click('页面LOGO')
        # log_case_info()
