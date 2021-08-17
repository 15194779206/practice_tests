import requests
import json
from Test_interface.lib.read_data import *
import unittest
from parameterized import parameterized
from Test_interface.lib.case_execute import *



class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @parameterized.expand([(case['case_name'],case) for case in get_data('Login', 'loginFail')])
    def test_1_loginFail(self,name, case):
        response=execute(case)
        if not response[1]:
            response[1] = json.loads(response[0].text)
        self.assertEqual(200, response[0].status_code, msg='用例%s响应异常'%case['id'])
        self.assertEqual(json.loads(case['req_exe']),response[1] ,msg='用例%s响应校检失败'%case['id'])


    @parameterized.expand([(case['case_name'], case) for case in get_data('Login','loginPass')])
    def test_2_loginPass(self, name, case):
        response = execute(case)
        if not response[1]:
            response[1] = json.loads(response[0].text)
        self.assertEqual(200, response[0].status_code, msg='用例%s响应异常' % case['id'])
        self.assertEqual(json.loads(case['req_exe']), response[1], msg='用例%s响应校检失败' % case['id'])

    # 错误三次出现图形验证码
    @parameterized.expand([(case['case_name'], case) for case in get_data('Login', 'loginFail3times')])
    def test_3_loginFailAppearCode(self, name, case):
        response = execute(case)
        if not response[1]:
            response[1] = json.loads(response[0].text)
        self.assertEqual(200, response[0].status_code, msg='用例%s响应异常' % case['id'])
        self.assertEqual(json.loads(case['req_exe']), response[1], msg='用例%s响应校检失败' % case['id'])

    # 手机验证码登录
    @parameterized.expand([(case['case_name'], case) for case in get_data('Login', 'loginMobile')])
    def test_4_loginFailMobile(self, name, case):
        response = execute(case)
        if not response[1]:
            response[1] = json.loads(response[0].text)
        self.assertEqual(200, response[0].status_code, msg='用例%s响应异常' % case['id'])
        self.assertEqual(json.loads(case['req_exe']), response[1], msg='用例%s响应校检失败' % case['id'])

    @classmethod
    def tearDownClass(cls):
        pass



#
# if __name__ == '__main__':
#     unittest.main()


