import requests
from parameterized.parameterized import *
import unittest
from Test_interface.lib.read_data import *
from Test_interface.lib.case_execute import *
import json

forgetPwd_ulr = 'https://test.kapbook.cn/resetpwd/set_login_pwd_ajax'
mobile_url ='https://test.kapbook.cn/resetpwd/verify_register_email_ajax'
# datas ={
#     'email':'15194779206',
#     'verify_code': '122222',
#     'password': '',
#     'nationcode_id': '214',
#     'nationcode': '86',}
# res= requests.post(url=forgetPwd_ulr, data=datas, headers=headers_choose())
# print(res.json())
class TestForgetPassword(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @parameterized.expand([(case['case_name'],case) for case in get_data('forgetPwd','mobilecheck')])
    def test_1_mobileCheck(self,name,case):
        response = execute(case)
        if not response[1]:
            response[1] = json.loads(response[0].text)
        self.assertEqual(200, response[0].status_code, msg='用例%s响应异常' % case['id'])
        self.assertEqual(json.loads(case['req_exe']), response[1], msg='用例%s响应校检失败' % case['id'])

    @parameterized.expand([(case['case_name'], case) for case in get_data('forgetPwd', 'resetPassword')])
    def test_2_resetPassword(self, name, case):
        response = execute(case)
        if not response[1]:
            response[1] = json.loads(response[0].text)
        self.assertEqual(200, response[0].status_code, msg='用例%s响应异常' % case['id'])
        self.assertEqual(json.loads(case['req_exe']), response[1], msg='用例%s响应校检失败' % case['id'])

    @classmethod
    def tearDownClass(cls):
        pass

# #
# if __name__ == '__main__':
#     unittest.main()
