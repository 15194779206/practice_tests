#读取管理员用户信息
from PO.login_page import *
from conf.conf import *
from lib.readfile import *
from selenium import webdriver


def login(driver, role):
    data_list = excel_to_list(data_file, "common_login")  # 读取该测试类所有用例数据
    case_list = get_test_data(data_list, role)  # 根据模块名称获取用例列表信息
    if not len(case_list):  # 有可能为None
        print("用例数据不存在")
    username = case_list[0]['username']
    password = case_list[0]['password']
    realname = case_list[0]['realname']
    url = test_env
    sp = LoginPage(driver)
    sp.open(url)
    sp.op_click('账号密码登录')
    sp.op_input('邮箱/手机号', username)
    sp.op_input('密码', password)
    sp.op_click('登录')
    return driver, realname
