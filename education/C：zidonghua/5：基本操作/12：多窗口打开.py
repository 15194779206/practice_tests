from selenium import webdriver
import time

dr=webdriver.Firefox()
dr.get("https://www.baidu.com/")
dr.maximize_window()
search_windows=dr.current_window_handle  #显示当前句柄
dr.find_element_by_link_text("登录").click()
time.sleep(2)
dr.find_element_by_link_text("立即注册").click()
time.sleep(2)
all_handls=dr.window_handles  #获取所有窗口句柄
for handle in all_handls:  #遍历所有的窗口句柄
    if handle !=search_windows:  #不等于当前句柄
        dr.switch_to_window(handle) #切换句柄，切换至注册页
        print("已切换至注册窗口")
        dr.find_element_by_name("userName").send_keys("user")
        dr.close() #只关闭当前窗口

dr.switch_to_window(search_windows)  #切换至登录窗口
dr.find_element_by_class_name("close-btn").click()