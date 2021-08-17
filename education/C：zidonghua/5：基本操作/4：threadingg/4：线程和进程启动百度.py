from threading import Thread
from selenium import webdriver
from time import sleep,ctime

def test_baidu(host,browser):
    print('start:%s'%ctime())
    print(host,browser)
    dc = {"browserName": browser}
    driver = webdriver.Remote(command_executor=host,
                          desired_capabilities=dc)

    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(browser)
    driver.find_element_by_id('su').click()
    driver.close()

if __name__ =='__main__':
    #启动参数，指定浏览器运行
    lists={'http://127.0.0.1:4444/wd/hub':'firefox',
           'http://127.0.0.1:6666/wd/hub':"chrome"}
    threads=[]
    files=range(len(lists))

    for host,browser in lists.items():
        t=Thread(target=test_baidu,args=(host,browser))
        threads.append(t)

    for  i in files:
        threads[i].start() #启动线程锁
    for i in files:
        threads[i].join()  #保护线程锁
    print('end:%s'%ctime())














































