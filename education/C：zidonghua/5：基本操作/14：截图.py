from selenium import  webdriver
driver=webdriver.Firefox()

driver.get("https://www.jiajiabank.com/")
# driver.find_element_by_xpath('//*[@id="__layout"]/section/div[1]/div/div[1]/div/a[1]')
driver.get_screenshot_as_file("D:\\baidu.jpg") #截图所存放位置