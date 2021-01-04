import time
class Login():
    def __init__(self,dr):
        self.dr=dr
    def login(self,usern,passw):

        one_iframe = self.dr.find_element_by_tag_name('iframe')
        self.dr.switch_to_frame(one_iframe)
        # element=WebDriverWait(dr,5,0.5).until(
        #     EC.presence_of_element_located(By.NAME,"email")
        # )
        # element.send_keys('lzhangnan')  #显示等待
        time.sleep(3)
        self.dr.find_element_by_name('email').send_keys(usern)
        self.dr.find_element_by_name('password').send_keys(passw)
        self.dr.find_element_by_id('dologin').click()
        self.dr.swich_to_default_content()
        print("登录成功")
    def loginout(self):
        pass