import unittest
from PO.equity_page import *
from PO.compList_page import *
from lib.login import *
from lib.log import *
from conf.conf import *
from time import sleep


class TestKapbookEquity(unittest.TestCase):
    """Kapbook期权/受限股授予流程测试"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)
        cls.url = test_env + certificate_list
        cls.driver, cls.name = login(cls.driver, '管理员')   #根据权限登录
        cls.sp = EquityPage(cls.driver)
        TestKapbookEquity.data_original = {}
        sp = CompListPage(cls.driver)
        sp.op_click('0705有限责任公司-虚拟股分红')

        cls.verificationErrors = []

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_1_options_new(self):
        """授予期权流程校验"""
        # 授予界面第1步的所有操作
        TestKapbookEquity.data_original = self.sp.op_check('第1条数据')
        self.sp.op_click('授予')
        self.sp.op_select('单人授予')
        self.sp.op_select('激励计划')
        self.sp.op_select('授予类型-期权')
        self.sp.op_select('协议模板-系统模板')
        self.sp.op_click('第1步-下一步')
        # 授予界面第2步的所有操作
        self.sp.op_select('姓名')
        self.sp.op_input('数量', '100')
        self.sp.op_input('授予日期', '2019-09-10')
        self.sp.op_input('行权单价', '0.10')
        self.sp.op_select('回购价格')
        self.sp.op_select('成熟计划')
        self.sp.op_input('成熟起算日', '2019-09-12')
        self.sp.op_click('第2步-下一步')
        # 授予界面最后一步的操作
        self.sp.op_click('完成')
        sleep(3)
        self.data_after = self.sp.op_check('第1条数据')
        try:
            self.assertNotEqual(TestKapbookEquity.data_original, self.data_after)
            log_case_info('Equity-1', '授予期权', 'PASS', '无', '只要id不是' + TestKapbookEquity.data_original['id'], self.data_after)
        except Exception as e:
            log_case_info('Equity-1', '授予期权', 'FAILED', '无', '只要id不是' + TestKapbookEquity.data_original['id'], self.data_after)

    def test_2_options_delete(self):
        """"删除草稿状态期权流程校验"""
        self.sp.op_click('操作')
        self.sp.op_select('删除草稿')
        self.sp.op_click('确认删除')
        sleep(3)
        self.data_delete = self.sp.op_check('第1条数据')
        try:
            self.assertEqual(TestKapbookEquity.data_original, self.data_delete)
            log_case_info('Equity-2', '删除草稿期权', 'PASS', '无', TestKapbookEquity.data_original, self.data_delete)
        except Exception as e:
            log_case_info('Equity-2', '删除草稿期权', 'FAILED', '无', TestKapbookEquity.data_original, self.data_delete)

    def test_3_restrictedStock_new(self):
        """授予受限股流程校验"""
        # 授予界面第1步的所有操作
        self.sp.op_click('受限股')
        TestKapbookEquity.data_original = self.sp.op_check('第1条数据')
        self.sp.op_click('授予')
        self.sp.op_select('单人授予')
        self.sp.op_select('激励计划')
        self.sp.op_select('授予类型-受限股')
        self.sp.op_select('协议模板-系统模板')
        self.sp.op_click('第1步-下一步')
        # 授予界面第2步的所有操作
        self.sp.op_select('姓名')
        self.sp.op_input('数量', '100')
        self.sp.op_select('代持股东')
        self.sp.op_input('授予日期', '2019-09-10')
        self.sp.op_input('行权单价', '0.10')
        self.sp.op_select('回购价格')
        self.sp.op_select('解限计划')
        self.sp.op_input('解限起算日', '2019-09-12')
        self.sp.op_click('第2步-下一步')
        # 授予界面最后一步的操作
        self.sp.op_click('完成')
        sleep(3)
        self.data_after = self.sp.op_check('第1条数据')
        try:
            self.assertNotEqual(TestKapbookEquity.data_original, self.data_after)
            log_case_info('Equity-3', '授予受限股', 'PASS', '无', '只要id不是' + TestKapbookEquity.data_original['id'], self.data_after)
        except Exception as e:
            log_case_info('Equity-3', '授予受限股', 'FAILED', '无', '只要id不是' + TestKapbookEquity.data_original['id'], self.data_after)

    def test_4_restrictedStock_delete(self):
        """"删除草稿状态受限股流程校验"""
        self.sp.op_click('操作')
        self.sp.op_select('删除草稿')
        self.sp.op_click('确认删除')
        sleep(3)
        self.data_delete = self.sp.op_check('第1条数据')
        try:
            self.assertEqual(TestKapbookEquity.data_original, self.data_delete)
            log_case_info('Equity-4', '删除草稿受限股', 'PASS', '无', TestKapbookEquity.data_original, self.data_delete)
        except Exception as e:
            log_case_info('Equity-4', '删除草稿受限股', 'FAILED', '无', TestKapbookEquity.data_original, self.data_delete)
