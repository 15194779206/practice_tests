from selenium import  webdriver
driver=webdriver.Firefox()

driver.get("https://www.jiajiabank.com/")
driver.set_window_size(600,500)
driver.execute_script("window.scrollTo(200,300)")  #x,y左右滚动
'''
#存在隐藏的情况下
js='document.querySelectorAll("select")[0].style.display="block";'
driver.execute_script(js)
'''
'''
#定位到此元素
ele=driver.find_element_by_xpath('/html/body/div/div[2]/section/div[3]/div[1]/div[1]/ul[2]/li[3]')
#固定用法
driver.execute_script('arguments[0].scrollIntoView()',ele)
ele.click()
'''