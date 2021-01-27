from Test_interface.lib.read_data import *
from Test_interface.lib.header_choose import *
import json
from parameterized.parameterized import *
import unittest
import requests
from bs4 import BeautifulSoup



class ModifyBank(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        login_datas = get_data('Login', 'loginPass')
        urls = 'https://test.kapbook.cn/login/check_login_ajax'
        datas = json.loads(next(login_datas).get('data'))
        response = requests.post(url=urls, data=datas)
        cls.times = response.cookies['request_time']
        cls.tokens = response.cookies['token']

        Save_company1 = 'https://test.kapbook.cn/user/index?from=login'
        company_list = requests.get(url=Save_company1, cookies=cookie, headers=header)
        # print(company_list.text)
        soup = BeautifulSoup(company_list.text, 'html.parser')
        dataToken_list = soup.find_all(class_='userVerify')
        tokens_list = [item.get('data-token') for item in dataToken_list]  # 获取company列表
        print(tokens_list)

    @parameterized.expand([(case['name'],case) for case in get_data('modifyBank','')])
    def test_1_modifyBank_fail(self):
        pass



    @classmethod
    def tearDownClass(cls):
        pass