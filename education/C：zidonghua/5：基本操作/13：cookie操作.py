from  selenium import webdriver

dr=webdriver.Firefox()
dr.get("https://www.baidu.com/")
dr.add_cookie({'name':'value','value':'values'})
for cookie in dr.get_cookies():
     print("%s--%s"%(cookie['name'],cookie['value']))
'''cookie=dr.get_cookies() #获取当前cookie值
print(cookie)'''
dr.quit()