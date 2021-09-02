import unittest
from PO.addParticipant_page import *
from lib.login import *
from lib.log import *
from PO.equity_page import *
from PO.compList_page import *
from conf.conf import *
from time import sleep
import os
import win32com.client

class TestKapbookAddPartcipant(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(2)
        cls.data_list = excel_to_list(data_file, "AddPartcipant_page")  # 读取该测试类所有用例数据
        cls.url = test_env + Participants_add
        cls.driver, cls.name = login(cls.driver, '管理员')
        TestKapbookAddPartcipant.data_original = {}   #类变量，类名+变量名，可进行调用操作
        cls.par = ParticipantPage(cls.driver)
        cls.sp = CompListPage(cls.driver)
        cls.sp.op_click('第一个企业有限公司')

    #添加数据校验
    def test_1_participant_new(self):
        time.sleep(1)
        self.par.op_click("公司管理")
        TestKapbookAddPartcipant.data_original = self.par.op_check("第1条数据")  # 未操作前获取数据
        TestKapbookAddPartcipant.data_origina2 = self.par.op_check("姓名和邮箱已存在")  # 未操作前获取数据
        self.par.op_click("添加参与方")
        case_list = get_test_data(self.data_list, 'participant_tab')  # 根据模块名称获取用例列表信息
        for case_data in case_list:  #读取数据
            if not case_data:  # 有可能为None
                print("用例数据不存在")
            case_id = case_data.get('case_id')
            case_name = case_data.get('case_name')
            username = case_data.get('username')
            email = case_data.get('email')
            certificate = case_data.get('certificate')
            ver_point = case_data.get('ver_point')
            expect_result = case_data.get('expect_result')
            certificate_type = case_data.get('certificate_type')
            authority_type = case_data.get('authority')
            company_name = case_data.get('company_name')
            legalPeople = case_data.get('legalPeople')
            credit_code = case_data.get('credit_code')

            if authority_type == "Natural_per":
                time.sleep(2)
                # self.par.op_click('自然人radio')
                self.par.op_input('姓名', username)
                self.par.op_input('邮箱', email)
                self.par.op_select("证件类型", certificate_type) #获取类型
                self.par.op_input('证件号', certificate)
                self.par.op_click('确定')

                if case_name == "输入正确":
                    name = []
                    mail = []
                    username = case_data.get('username')
                    email = case_data.get('email')
                    name.append(username)
                    mail.append(email)
                    data = dict(zip(name, mail))
                    for i in TestKapbookAddPartcipant.data_origina2:
                        for y in data:
                            if TestKapbookAddPartcipant.data_origina2[i] == data[y]:
                                sleep(3)
                                self.par.op_input('邮箱', '123422@qq.com')
                                self.par.op_input('证件号', '123344ll')
                                self.par.op_click('确定')
                            else:
                                pass
                    self.par.op_click('小程序确定Btn')
                    self.par.op_click("添加参与方")

            elif authority_type == "Legal_person":
                # time.sleep(2)
                # self.par.op_click("添加参与方")
                time.sleep(2)
                self.par.op_click('法人radio')
                time.sleep(2)
                self.par.op_input('企业名称', company_name)
                self.par.op_click('负责人姓名')
                self.par.op_input('信用代码', credit_code)
                self.par.op_click("营业执照")
                sleep(3)
                shell = win32com.client.Dispatch("WScript.Shell")
                shell.Sendkeys(r"C:\Users\lenovo\Desktop\pic\1.jpg"+"{Enter}{Enter}")
                sleep(2)
                self.par.op_click('法人确定添加')
                time.sleep(2)

        self.data_after = self.par.op_check('第1条数据')  # 获取新添加的数据
        try:
            self.assertNotEqual(TestKapbookAddPartcipant.data_original, self.data_after)
            log_case_info('AddPartcipant_1', '添加参与方', 'PASS', '无', '只要id不是' + TestKapbookAddPartcipant.data_original['id'], self.data_after)
        except Exception as e:
            log_case_info('AddPartcipant_1', '添加参与方', 'FAILED', '无', '只要id不是' + TestKapbookAddPartcipant.data_original['id'],self.data_after)

    def test_3_participant_delete(self):
        time.sleep(2)
        # self.par.op_click('确定')
        self.par.op_click("编辑")
        self.par.op_click("删除")
        self.par.op_click("确定_删除")
        sleep(3)
        self.data_delete = self.par.op_check('第1条数据')
        try:
            self.assertEqual(TestKapbookAddPartcipant.data_original, self.data_delete)
            log_case_info('AddPartcipant_2', '删除草稿参与方', 'PASS', '无', TestKapbookAddPartcipant.data_original, self.data_delete)
        except Exception as e:
            log_case_info('AddPartcipant_2', '删除草稿参与方', 'FAILED', '无', TestKapbookAddPartcipant.data_original, self.data_delete)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

