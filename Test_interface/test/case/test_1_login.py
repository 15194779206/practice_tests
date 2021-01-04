import requests
import json
from Test_interface.lib.read_data import *
import unittest
from parameterized import parameterized
from Test_interface.config.config import *



base_login = '/login/check_login_ajax'
base_login2 = '/login/check_login_by_mobile_ajax'
base_save_company = '/user/save_company_info_ajax'
Login_url = BaseUrl+base_login
Login_url2 = BaseUrl+base_login2
Save_company = BaseUrl+base_save_company

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @parameterized.expand([(case['case_name'],case) for case in get_data('Login', 'loginFail')])
    def test_1_loginFail(self,name, case):
        datas =json.loads(case.get('data'))
        response = requests.post(url=Login_url, data=datas)
        self.assertEqual(response.json(),json.loads(case.get('req_exe')),"实际与预期不符")

    @parameterized.expand([(case['case_name'], case) for case in get_data('Login','loginPass')])
    def test_2_loginPass(self, name, case):
        datas = json.loads(case.get('data'))
        response = requests.post(url=Login_url, data=datas)
        self.assertEqual(response.json(), json.loads(case.get('req_exe')), "实际与预期不符")

    # 错误三次出现图形验证码
    @parameterized.expand([(case['case_name'], case) for case in get_data('Login', 'loginFail3times')])
    def test_3_loginFailAppearCode(self, name, case):
        datas = json.loads(case.get('data'))
        response = requests.post(url=Login_url, data=datas)
        self.assertEqual(response.json(), json.loads(case.get('req_exe')), "实际与预期不符")

    # 手机验证码登录
    @parameterized.expand([(case['case_name'], case) for case in get_data('Login', 'loginMobile')])
    def test_4_loginFailMobile(self, name, case):
        datas = json.loads(case.get('data'))
        response = requests.post(url=Login_url2, data=datas)
        self.assertEqual(response.json(), json.loads(case.get('req_exe')), "实际与预期不符")

    @classmethod
    def tearDownClass(cls):
        pass




if __name__ == '__main__':
    unittest.main()


