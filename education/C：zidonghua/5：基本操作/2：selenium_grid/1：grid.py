from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import  DesiredCapabilities
#4444为端口号，
#第二种用法： desired_capabilities=DesiredCapabilities.FIREFOX
dr=webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
                    desired_capabilities={
                        "browserName":"chrome",
                        "version":"",
                        "platform":"ANY",
                        "javascriptEnabled":True,
                    })
dr.get('http://baidu.com')
dr.find_element_by_id("kw").send_keys("selenium")
dr.find_element_by_id("su").click()
# dr.close()