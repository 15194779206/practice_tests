from Test_interface.lib.read_data import *
from Test_interface.lib.header_choose import *
import json
from parameterized.parameterized import *
import unittest
import requests
from bs4 import BeautifulSoup
from Test_interface.lib.send_request import *
from  Test_interface.common.enter_company import *
from Test_interface.lib.case_execute import *



class ModifyBank(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        login_datas = get_data('Login', 'loginPass')
        response = send_request(next(login_datas))
        cls.times = response.cookies['request_time']
        cls.tokens = response.cookies['token']


    @parameterized.expand([(case['case_name'],case) for case in get_data('modifyBank','SavePass')])
    def test_1_modifyBank_fail(self,name,case):
        company_token = enter_company(self.times, self.tokens)
        response = execute(case, cookie={'token': self.tokens, 'request_time': self.times,'company_token':company_token})
        if not response[1]:
            response[1] = json.loads(response[0].text)
        self.assertEqual(200, response[0].status_code, msg='用例%s响应异常' % case['id'])


    @classmethod
    def tearDownClass(cls):
        pass
#
# if __name__ == '__main__':
#     unittest.main()

