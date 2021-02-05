from Test_interface.lib.read_data import *
import requests
import unittest
from parameterized import parameterized
from Test_interface.config.config import *
import json
from bs4 import BeautifulSoup
from Test_interface.lib.header_choose import *
from Test_interface.lib.header_choose import *


class Creat_company(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        login_datas = get_data('Login','loginPass')
        urls = 'https://test.kapbook.cn/login/check_login_ajax'
        datas =json.loads(next(login_datas).get('data'))
        response = requests.post(url=urls, data=datas,headers=headers_choose())
        cls.times = response.cookies['request_time']
        cls.tokens = response.cookies['token']


    @parameterized.expand([(case['case_name'],case) for case in get_data('addCompany','ShowList')])
    def test_1_creatCompany_pass(self,name,case):
        cookies = json.loads(case.get('cookies'))
        if cookies['request_time']:
            cookies['request_time'] = self.times
        else:
            cookies['request_time'] = None
        if cookies['token']:
            cookies['token'] = self.tokens
        else:
            cookies['token'] = None
        com_urls =BaseUrl+case.get('url')
        response= requests.get(url=com_urls,cookies=cookies,headers=headers_choose())
        soup = BeautifulSoup(response.text,'html.parser')
        self.assertEqual(soup.title.text, case.get('req_exe'))

    @parameterized.expand([(case['case_name'], case) for case in get_data('addCompany', 'SavePass')])
    def test_1_creatCompany_pass(self, name, case):
        cookies = json.loads(case.get('cookies'))
        datas = json.loads(case.get('data'))
        if cookies['request_time']:
            cookies['request_time'] = self.times
        else:
            cookies['request_time'] = None
        if cookies['token']:
            cookies['token'] = self.tokens
        else:
            cookies['token'] = None
        com_urls = BaseUrl + case.get('url')
        response = requests.post(url=com_urls, cookies=cookies,data=datas,headers=headers_choose())
        self.assertEqual(response.json(), json.loads(case.get('req_exe')))

    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()
