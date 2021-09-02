from selenium.webdriver.common.by import By
from PO import base_page


class RegisterPage(base_page.Action):
    btn_start = (By.ID, "reg_start")
    btn_getCode = (By.CSS_SELECTOR, "#sendcodeBtn")
    btn_login = (By.CSS_SELECTOR, ".login_header > a")
    input_tel = (By.CSS_SELECTOR, "#mobile_mobile")
    input_code = (By.CSS_SELECTOR, "#mobileCode")
    logo_index = (By.CSS_SELECTOR, ".login_header > .fl")
    alert_tel = (By.CSS_SELECTOR, "#mobile_mobile + div > em")
    alert_code = (By.CSS_SELECTOR, "#mobileCode + a + div > em")
    link_provision = (By.CSS_SELECTOR, ".go_login")

    def op_click(self, obj):
        if obj == '立刻开始体验':
            self.find_element(*self.btn_start).click()
        elif obj == '登录':
            self.find_element(*self.btn_login).click()
        elif obj == '获取验证码':
            self.find_element(*self.btn_getCode).click()
        elif obj == '页面LOGO':
            self.find_element(*self.logo_index).click()
        elif obj == '隐私条款':
            self.find_element(*self.link_provision).click()

    def op_input(self, obj, string):
        if obj == '手机号':
            self.send_keys(self.input_tel, string)
        elif obj == '验证码':
            self.send_keys(self.input_code, string)

    def show_alert(self, obj):
        if obj == '手机号提示':
            try:
                self.alert = self.find_element(*self.alert_tel)
                return self.alert.text
            except Exception as e:
                return self.alert
        elif obj == '验证码提示':
            try:
                self.alert = self.find_element(*self.alert_code)
                return self.alert.text
            except Exception as e:
                return self.alert
