from selenium import webdriver
import time

dr=webdriver.Firefox()
dr.get('https://www.126.com/')

one_iframe=dr.find_element_by_tag_name('iframe')
dr.switch_to_frame(one_iframe)
# element=WebDriverWait(dr,5,0.5).until(
#     EC.presence_of_element_located(By.NAME,"email")
# )
# element.send_keys('lzhangnan')  #显示等待
time.sleep(3)
dr.find_element_by_name('email').send_keys('lzhangnan')
dr.find_element_by_name('password').send_keys('131214ly')
dr.find_element_by_id('dologin').click()
dr.swich_to_default_content()
print("登录成功")