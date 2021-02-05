import requests
from Test_interface.lib.header_choose import *
from parameterized.parameterized import *
import unittest
from Test_interface.lib.read_data import *
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
        data = json.loads(case.get('data'))
        response = requests.post(url=mobile_url, data=data, headers=headers_choose())
        self.assertEqual(response.json(),json.loads(case['req_exe']),"预期与实际不符")

    @parameterized.expand([(case['case_name'], case) for case in get_data('forgetPwd', 'resetPassword')])
    def test_2_resetPassword(self, name, case):
        data = json.loads(case.get('data'))
        response = requests.post(url=mobile_url, data=data, headers=headers_choose())
        self.assertEqual(response.json(), json.loads(case['req_exe']), "预期与实际不符")

    @classmethod
    def tearDownClass(cls):
        pass

#
if __name__ == '__main__':
    unittest.main()
