from selenium.webdriver.common.by import By
from PO import base_page


class LoginPage(base_page.Action):
    btn_login = (By.ID, "login_ajax")
    btn_getCode = (By.CSS_SELECTOR, "#sendcodeBtn")
    btn_register = (By.CSS_SELECTOR, ".login_header > a")
    alert_user = (By.CSS_SELECTOR, "#email + div > em")
    alert_pwd = (By.CSS_SELECTOR, "#password + div > em")
    alert_tel = (By.CSS_SELECTOR, "#phone + div > em")
    alert_code = (By.CSS_SELECTOR, "#phoneCode + a + div > em")
    tab_tel = (By.CSS_SELECTOR, ".login_li > .newLogin")
    tab_user = (By.CSS_SELECTOR, ".login_li > .oldLogin")
    input_user = (By.CSS_SELECTOR, "#email")
    input_pwd = (By.CSS_SELECTOR, "#password")
    input_tel = (By.CSS_SELECTOR, "#phone")
    input_code = (By.CSS_SELECTOR, "#phoneCode")
    link_resetPWD = (By.CSS_SELECTOR, ".forget")
    logo_index = (By.CSS_SELECTOR, ".login_header > .fl")

    def op_click(self, obj):
        if obj == '登录':
            self.find_element(*self.btn_login).click()
        elif obj == '注册':
            self.find_element(*self.btn_register).click()
        elif obj == '获取验证码':
            self.find_element(*self.btn_getCode).click()
        elif obj == '手机验证码登录':
            self.find_element(*self.tab_tel).click()
        elif obj == '账号密码登录':
            self.find_element(*self.tab_user).click()
        elif obj == '忘记密码':
            self.find_element(*self.link_resetPWD).click()
        elif obj == '页面LOGO':
            self.find_element(*self.logo_index).click()

    def op_input(self, obj, string):
        if obj == '邮箱/手机号':
            self.send_keys(self.input_user, string)
        elif obj == '密码':
            self.send_keys(self.input_pwd, string)
        elif obj == '手机号':
            self.send_keys(self.input_tel, string)
        elif obj == '验证码':
            self.send_keys(self.input_code, string)

    def show_alert(self, obj):
        if obj == '邮箱/手机号提示':
            return self.find_element(*self.alert_user).text
        elif obj == '密码提示':
            return self.find_element(*self.alert_pwd).text
        elif obj == '手机号提示':
            return self.find_element(*self.alert_tel).text
        elif obj == '验证码提示':
            return self.find_element(*self.alert_code).text
