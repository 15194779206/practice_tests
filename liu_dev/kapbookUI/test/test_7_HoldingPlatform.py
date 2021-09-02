import unittest
from PO.HoldingPlatform_page import *
from lib.log import *
from lib.login import *
from PO.compList_page import *
from conf.conf import *
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class TestKapbookaddPlatform(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(3)
        cls.data_list = excel_to_list(data_file, "holdingPlatform")  # 读取该测试类所有用例数据
        cls.url = test_env + holdPlatform
        cls.driver, cls.name = login(cls.driver, '管理员')
        TestKapbookaddPlatform.data_original = {}  # 类变量，类名+变量名，可进行调用操作
        cls.hold = HoldplatformPage(cls.driver)
        cls.sp = CompListPage(cls.driver)
        cls.sp.op_click('第一个企业有限公司')


    def test_1_liability_add(self):
        # TestKapbookaddPlatform.data_original = self.sp.op_check('第1条数据')
        time.sleep(3)
        self.hold.op_click("公司管理")
        self.hold.op_move("公司管理")
        # ele = self.hold.op_move("公司管理")
        # ActionChains(self.driver).move_to_element(ele).perform()
        sleep(3)
        self.hold.op_click('持股平台')
        self.hold.op_click('添加持股平台')
        self.hold.op_click('单层持股平台')
        case_list = get_test_data(self.data_list, 'participant_tab')
        for case_data in case_list:
            if not case_list:
                print("用例数据不存在")
            case_id = case_data.get('case_id')
            step_type = case_data.get('step_type')
            case_name = case_data.get('case_name')
            ver_point = case_data.get('ver_point')  #提示所在区域
            platform_name = case_data.get('platform_name') #企业名称
            platform_captical = case_data.get('platform_captical')  #注册资本
            platform_Shares = case_data.get('platform_Shares') #持有资本
            memberShare = case_data.get('memberShare') #注册资本输入
            memberSharePay = case_data.get('memberSharePay')  #实缴金额
            BankName = case_data.get('BankName')  #开户行
            BankNum = case_data.get('BankNum')   #账号
            into_list = case_data.get("into_list")

            if step_type == "base_info":
                self.hold.op_input('公司名称', platform_name)
                self.hold.op_select("公司类型-责任")
                self.hold.op_input("基本信息-注册资本", platform_captical)
                self.hold.op_input("基本信息-持有资本", platform_Shares)
                self.hold.op_click("基本信息-下一步")
                if ver_point == 'company_name':
                    actual_result = self.hold.show_alert('名称文本提示')
                elif ver_point == 'company_captical':
                    actual_result = self.hold.show_alert('注册资本提示')
                elif ver_point == 'company_shares':
                    actual_result = self.hold.show_alert('持有资本提示')
                elif ver_point == 'alert_company':
                    actual_result = self.hold.show_alert("弹出框提示")
                    self.hold.op_click("fir弹出框btn")

            elif step_type == "share_info":    #股权信息页面
                self.hold.op_click("添加股东btn")
                self.hold.op_select("first股东添加")

                self.hold.op_input("注册资本", memberShare)
                self.hold.op_input("实缴金额", memberSharePay)
                self.hold.op_click("注册资本页-确定")
                # if ver_point == 'memberShare_text':
                #     actual_result = self.hold.show_alert('sec注册资本text')
                # elif ver_point == 'sharePay_text':
                #     actual_result = self.hold.show_alert('sec实缴金额text')
                self.hold.op_select("second股东添加")
                self.hold.op_input("注册资本", memberShare)
                self.hold.op_input("实缴金额", memberSharePay)
                self.hold.op_click("注册资本页-确定")
                self.hold.op_click("股权信息-下一步")

            elif step_type == "transferor":  #代持人页面
                self.hold.op_select("代持人-代持人sel")
                self.hold.op_input("代持人-注册资本", memberShare)
                self.hold.op_click("代持人-下一步")
            elif step_type == "BankInfo":
                self.hold.op_input("对公账户-开户行", BankName)
                self.hold.op_input("对公账户-账号", BankNum)
                self.hold.op_click("对公账户-下一步")
                time.sleep(2)
                one = self.hold.op_move("预览-确定")
                self.driver.execute_script('arguments[0].scrollIntoView()', one)
                one.click()
                sleep(2)
                self.hold.op_click('我知道了')
                self.hold.op_click('操作')
                self.hold.op_click('设为草稿select')
                self.hold.op_click("设为草稿btn")
                time.sleep(2)
                self.hold.op_click('操作')
                self.hold.op_click("删除持股平台")


