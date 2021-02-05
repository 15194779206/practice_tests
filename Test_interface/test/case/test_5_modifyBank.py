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
        login_datas = get_data('Login','loginPass')
        urls = 'https://test.kapbook.cn/login/check_login_ajax'
        datas = json.loads(next(login_datas).get('data'))
        response = requests.post(url=urls, data=datas,headers=headers_choose())
        cls.times = response.cookies['request_time']
        cls.tokens = response.cookies['token']
        cookie={
            "request_time": cls.times,
            "token": cls.tokens
        }
        Save_company1 = 'https://test.kapbook.cn/user/index?from=login'
        company_list = requests.get(url=Save_company1, cookies=cookie, headers=headers_choose())
        # print(company_list.text)
        soup = BeautifulSoup(company_list.text, 'html.parser')
        dataToken_list = soup.find_all(class_='userVerify')
        cls.tokens_list = [item.get('data-token') for item in dataToken_list]  # 获取company列表
        print(cls.tokens_list)


    @parameterized.expand([(case['case_name'],case) for case in get_data('modifyBank','SavePass')])
    def test_1_modifyBank_fail(self,name,case):
        cookies = json.loads(case.get('cookies'))
        data2 = json.loads(case.get('data'))
        if cookies['request_time']:
            cookies['request_time'] = self.times
        else:
            cookies['request_time'] = None
        if cookies['token']:
            cookies['token'] = self.tokens
        else:
            cookies['token'] = None
        if cookies['company_token']:
            cookies['company_token'] = self.tokens_list[0]
        else:
            cookies['company_token'] = None
        modifyBank_url = 'https://test.kapbook.cn/company/setting/operate_corporate_account'
        response_req = requests.post(url=modifyBank_url, cookies=cookies,data=data2,headers= headers_choose())
        self.assertEqual(response_req.json(), json.loads(case.get('req_exe')))

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main()

