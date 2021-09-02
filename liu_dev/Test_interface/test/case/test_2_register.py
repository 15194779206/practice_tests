from selenium import webdriver
from parameterized import *
import json
import unittest
from Test_interface.lib.read_data import *
from Test_interface.lib.case_execute import *

class TestUserRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @parameterized.expand([(case['case_name'],case) for case in get_data('Register','checkoutMoblie')])
    def test_1_registerPass(self,name,case):
        response = execute(case)
        if not response[1]:
            response[1] = json.loads(response[0].text)
        self.assertEqual(200, response[0].status_code, msg='用例%s响应异常' % case['id'])
        self.assertEqual(json.loads(case['req_exe']), response[1], msg='用例%s响应校检失败' % case['id'])

    @parameterized.expand([(case['case_name'], case) for case in get_data('Register', 'registerAajax')])
    def test_1_registerPass(self, name, case):
        response = execute(case)
        if not response[1]:
            response[1] = json.loads(response[0].text)
        self.assertEqual(200, response[0].status_code, msg='用例%s响应异常' % case['id'])
        self.assertEqual(json.loads(case['req_exe']), response[1], msg='用例%s响应校检失败' % case['id'])


    @classmethod
    def tearDownClass(cls):
        pass


# if __name__ == '__main__':
#     unittest.main()