from selenium.webdriver.common.by import By
from PO import base_page


class ResetPwdPage(base_page.Action):
    btn_submit = (By.ID, "login_ajax")
    btn_getCode = (By.CSS_SELECTOR, "#sendcodeBtn")
    btn_login = (By.CSS_SELECTOR, ".login_header > a")
    input_user = (By.CSS_SELECTOR, "#email")
    input_code = (By.CSS_SELECTOR, "#code")
    input_newPWD = (By.CSS_SELECTOR, "#password")
    logo_index = (By.CSS_SELECTOR, ".login_header > .fl")
    alert_user = (By.CSS_SELECTOR, "#email + div > em")
    alert_code = (By.CSS_SELECTOR, "#code + a + div > em")
    alert_newPWD = (By.CSS_SELECTOR, "#password + div > em")

    def op_click(self, obj):
        if obj == '提交':
            self.find_element(*self.btn_submit).click()
        elif obj == '登录':
            self.find_element(*self.btn_login).click()
        elif obj == '获取验证码':
            self.find_element(*self.btn_getCode).click()
        elif obj == '页面LOGO':
            self.find_element(*self.logo_index).click()

    def op_input(self, obj, string):
        if obj == '邮箱/手机号':
            self.send_keys(self.input_user, string)
        elif obj == '验证码':
            self.send_keys(self.input_code, string)
        elif obj == '新密码':
            self.send_keys(self.input_newPWD, string)

    def show_alert(self, obj):
        if obj == '邮箱/手机号提示':
            return self.find_element(*self.alert_user).text
        elif obj == '验证码提示':
            return self.find_element(*self.alert_code).text
        elif obj == '新密码提示':
            return self.find_element(*self.alert_newPWD).text
