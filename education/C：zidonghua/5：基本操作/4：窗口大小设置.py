from selenium import webdriver
driver=webdriver.Firefox()
driver.get("https://www.baidu.com/")
#设置固定宽高的浏览器
driver.set_window_size(1000,1000)   #set_window_size(宽，高)
#窗口最大化
driver.maximize_window()
# driver.quit()