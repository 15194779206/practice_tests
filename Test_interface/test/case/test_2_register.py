from selenium import webdriver
from parameterized import *
import json
import unittest
from Test_interface.lib.read_data import *
import requests
regiser_url ="https://test.kapbook.cn/register/check_mobile"

class TestUserRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @parameterized.expand([(case['case_name'],case) for case in get_data('Register','regeiserPass')])
    def test_1_registerPass(self,name,case):
        datas = json.loads(case['data'])
        response = requests.post(url=regiser_url,data=datas)
        self.assertEqual(response.json(),json.loads(case['req_exe']),"预期与实际不符")


    @classmethod
    def tearDownClass(cls):
        pass


if __name__ == '__main__':
    unittest.main()