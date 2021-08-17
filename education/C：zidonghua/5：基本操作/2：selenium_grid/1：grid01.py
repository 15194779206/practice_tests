from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities

#获取浏览器名称
# F:\anzhuang\python3.6\Lib\site-packages\selenium\webdriver\common里面的desir...
shuzu=["chrome","firefox","internet explorer"]
for browser in shuzu:
    browser={"browserName":browser}
    dr=webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                        desired_capabilities=browser)

    dr.get('http://baidu.com')
    dr.find_element_by_id("kw").send_keys("selenium")
    dr.find_element_by_id("su").click()
    # dr.close()














