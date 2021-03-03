from Test_interface.lib.read_data import *
import requests
import unittest
from parameterized import parameterized
import json
from bs4 import BeautifulSoup
from Test_interface.lib.send_request import *
from Test_interface.lib.case_execute import *


class Creat_company(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        login_datas = get_data('Login','loginPass')
        response =send_request(next(login_datas))
        cls.times = response.cookies['request_time']
        cls.tokens = response.cookies['token']


    @parameterized.expand([(case['case_name'],case) for case in get_data('addCompany','SavePass')])
    def test_1_creatCompany_pass(self,name,case):
        response = execute(case,cookie={'token': self.tokens, 'request_time': self.times})
        if not response[1]:
            response[1] = json.loads(response[0].text)
        self.assertEqual(200, response[0].status_code, msg='用例%s响应异常' % case['id'])
        self.assertEqual(json.loads(case['req_exe']), response[1], msg='用例%s响应校检失败' % case['id'])
        soup = BeautifulSoup(response.text, 'html.parser')
        self.assertEqual(soup.title.text, case.get('req_exe'))

    @classmethod
    def tearDownClass(cls):
        pass


#title判断存在问题
'''
    @parameterized.expand([(case['case_name'], case) for case in get_data('addCompany', 'ShowList')])
    def test_1_creatCompany_pass(self, name, case):
        cookies = json.loads(case.get('cookies'))
        BaseUrl = 'https://test.kapbook.cn'
        if cookies['request_time']:
            cookies['request_time'] = self.times
        else:
            cookies['request_time'] = None
        if cookies['token']:
            cookies['token'] = self.tokens
        else:
            cookies['token'] = None
        com_urls = BaseUrl + case.get('url')
        response = requests.get(url=com_urls, cookies=cookies,headers=headers_choose())
        # response = execute(case, cookie={'token': self.tokens, 'request_time': self.times})
        soup = BeautifulSoup(response.text, 'html.parser')
        self.assertEqual(soup.title.text, case.get('req_exe'))
'''



if __name__ == '__main__':
    unittest.main()
