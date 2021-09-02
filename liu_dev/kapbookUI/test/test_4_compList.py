import unittest
from PO.compList_page import *
from lib.login import *
from lib.log import *
from conf.conf import *


class TestKapbookCompList(unittest.TestCase):
    """Kapbook公司选择页面 UI自动化登录"""
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.url = test_env + user
        # self.verificationErrors = []

    def test_1_admin_check(self):
        """管理员登录后公司列表页登录状态校验"""
        self.driver, self.name = login(self.driver, '管理员')
        sp = CompListPage(self.driver)
        realname = sp.show_text('当前用户姓名')
        try:
            self.assertEqual(self.name, realname)
            log_case_info('CompList-1', '管理员登录', 'PASS', '无', self.name, realname)
        except Exception as e:
            log_case_info('CompList-1', '管理员登录', 'FAILED', '无', self.name, realname)

    def test_2_admin_menu(self):
        """管理员登录后公司列表页消息校验"""
        sp = CompListPage(self.driver)
        menu_info = '，'.join(sp.show_text('导航菜单'))
        try:
            # self.assertEqual(msg_icon_num, msg_banner_num)
            log_case_info('CompList-2', '管理员菜单', 'PASS', '无', menu_info, menu_info)
        except Exception as e:
            log_case_info('CompList-2', '管理员菜单', 'FAILED', '无', menu_info, menu_info)
        # sp.mouse_suspension('当前用户姓名')
        # sp.op_click('退出登录')

    def test_3_admin_msg(self):
        """管理员登录后公司列表页消息校验"""
        sp = CompListPage(self.driver)
        msg_icon_num = sp.show_text('消息图标未读数量')
        msg_banner_num = sp.show_text('banner提示')
        try:
            self.assertEqual(msg_icon_num, msg_banner_num)
            log_case_info('CompList-3', '未读消息校验', 'PASS', '无', msg_icon_num, msg_banner_num)
        except Exception as e:
            log_case_info('CompList-3', '未读消息校验', 'FAILED', '无', msg_icon_num, msg_banner_num)
        # sp.mouse_suspension('当前用户姓名')
        # sp.op_click('退出登录')

    def test_4_normal_user_check(self):
        """一般用户登录后公司列表页登录状态校验"""
        self.driver, self.name = login(self.driver, '一般用户')
        sp = CompListPage(self.driver)
        realname = sp.show_text('当前用户姓名')
        try:
            self.assertEqual(self.name, realname)
            log_case_info('CompList-4', '一般用户登录', 'PASS', '无', self.name, realname)
        except Exception as e:
            log_case_info('CompList-4', '一般用户登录', 'FAILED', '无', self.name, realname)
        # sp.mouse_suspension('当前用户姓名')
        # sp.op_click('退出登录')

    def test_5_normal_user_menu(self):
        """一般用户登录后公司列表页消息校验"""
        sp = CompListPage(self.driver)
        menu_info = '，'.join(sp.show_text('导航菜单'))
        try:
            # self.assertEqual(msg_icon_num, msg_banner_num)
            log_case_info('CompList-5', '一般用户菜单', 'PASS', '无', menu_info, menu_info)
        except Exception as e:
            log_case_info('CompList-5', '一般用户菜单', 'FAILED', '无', menu_info, menu_info)
        sp.mouse_suspension('当前用户姓名')
        sp.op_click('退出登录')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
