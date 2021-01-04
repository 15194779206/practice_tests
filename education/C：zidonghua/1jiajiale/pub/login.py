import time

def login(driver,user,passw):
    driver.find_element_by_xpath('/html/body/div[3]/div[12]/div[3]').click()
    driver.find_element_by_link_text("登录").click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="signup-form"]/div[1]/input').send_keys(user)
    driver.find_element_by_xpath('//*[@id="signup-form"]/div[2]/input').send_keys(passw)
    driver.find_element_by_xpath('//*[@id="signup-form"]/div[5]').click()
