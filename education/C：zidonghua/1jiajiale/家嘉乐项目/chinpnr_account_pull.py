#!/usr/bin/python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='bankbyjiajia', charset="utf8",
                     use_unicode=True)


def insert(data):
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = "INSERT INTO tb_chinapnr_account_detail(create_time, \
       serial_number, usr_id, user_name, acct_type,debit_or_credit_mark,tran_amount,free_amount,acct_amount,in_usr_id,buss_type,des_note) \
       VALUES ('%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s','%s','%s','%s')" % \
          (data[0], data[1], data[2], data[3], data[4], data[5], data[6].replace(',', ''), data[7].replace(',', ''),
           data[8].replace(',', ''), data[9], data[10], data[11])
    # try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    # except:
    # 发生错误时回滚
    # db.rollback()


usrids = ['6000060269448244', '6000060269448119', '6000060269453923', '6000060269456948', '6000060269455093',
          '6000060269455994', '6000060269459071', '6000060269455869', '6000060269456118', '6000060269456261',
          '6000060269457616', '6000060269462708', '6000060269461736', '6000060269463618', '6000060269652085',
          '6000060269469033', '6000060269480234', '6000060269480225', '6000060269488245', '6000060269554011',
          '6000060269572475', '6000060269586521', '6000060269591533', '6000060269593773', '6000060269693585',
          '6000060269697796', '6000060269696840', '6000060269699222', '6000060269764954', '6000060269743638',
          '6000060269785094', '6000060269786761', '6000060269810654', '6000060269826745', '6000060269918708',
          '6000060269935173', '6000060269938241', '6000060269943716', '6000060269968627', '6000060269971043',
          '6000060269974255', '6000060269991218', '6000060269996017', '6000060270007753', '6000060269998792',
          '6000060270012462', '6000060270016379', '6000060273437908', '6000060270080487', '6000060270084474',
          '6000060270088461', '6000060270122389', '6000060270120452', '6000060270130888', '6000060270167777',
          '6000060270178319', '6000060270182545', '6000060270187327', '6000060270193123', '6000060270194961',
          '6000060270196585', '6000060270197334', '6000060270207724', '6000060270245666', '6000060270250454',
          '6000060270290465', '6000060270326597', '6000060270329727', '6000060270457918', '6000060270711545',
          '6000060270777172', '6000060270787884', '6000060270839686', '6000060270979347', '6000060271138986',
          '6000060271413848', '6000060271429555', '6000060271431891', '6000060271441461', '6000060271607309',
          '6000060271765842', '6000060272137958', '6000060272216676', '6000060272235138', '6000060272451778',
          '6000060272579695', '6000060272620195', '6000060272734740', '6000060272779728', '6000060272799975',
          '6000060272947208', '6000060273017933', '6000060273037378', '6000060273060715', '6000060273155882',
          '6000060273210947', '6000060273239329', '6000060273302928', '6000060273307834', '6000060273329213',
          '6000060273503970', '6000060273545952', '6000060273554273', '6000060273573797', '6000060273581476',
          '6000060273617081', '6000060274035680', '6000060274038213', '6000060274239176', '6000060274334081',
          '6000060274348254', '6000060274510041', '6000060274544880', '6000060274532900', '6000060274624847',
          '6000060274628594', '6000060274654234', '6000060274684899', '6000060274750102', '6000060274750219',
          '6000060274857284', '6000060274897106', '6000060274974772', '6000060281109604', '6000060275043945',
          '6000060275068712', '6000060275074965', '6000060275083919', '6000060275148351', '6000060275157082',
          '6000060275207206', '6000060275277050', '6000060275367596', '6000060275397705', '6000060275426041',
          '6000060275440999', '6000060275465481', '6000060275543272', '6000060275603634', '6000060275839738',
          '6000060275852561', '6000060275977669', '6000060276008278', '6000060276077924', '6000060276088912',
          '6000060276095165', '6000060276333693', '6000060276564979', '6000060276506649', '6000060276541076',
          '6000060276697942', '6000060276699325', '6000060276705498', '6000060276803541', '6000060276890992',
          '6000060277250182', '6000060277256024', '6000060277353197', '6000060277439532', '6000060277397532',
          '6000060277416897', '6000060277551776', '6000060278336455', '6000060278760851', '6000060280233099',
          '6000060280355359', '6000060280459078', '6000060280462643', '6000060280616069', '6000060280638063',
          '6000060280807932', '6000060280816352', '6000060280827876', '6000060281093176', '6000060281190999',
          '6000060281237413', '6000060281349695', '6000060281474013', '6000060281607816', '6000060281871398',
          '6000060281894104', '6000060281940983', '6000060281943249', '6000060281948468', '6000060281951239',
          '6000060282077968', '6000060282137644', '6000060282182522', '6000060282311535', '6000060282710505',
          '6000060282717438', '6000060282742464', '6000060282989858', '6000060283127582', '6000060283130426',
          '6000060283534963', '6000060283674197', '6000060283766962', '6000060283907622', '6000060284026975',
          '6000060284270807', '6000060284481606', '6000060284562617', '6000060284596038', '6000060284630143',
          '6000060284785850', '6000060284935948', '6000060284839400', '6000060284931568', '6000060285006663',
          '6000060285020576', '6000060285032126', '6000060285046175', '6000060285140278', '6000060285234195',
          '6000060285338298', '6000060285405642', '6000060285407551', '6000060285416934', '6000060285740076',
          '6000060285780870', '6000060285804863', '6000060285887505', '6000060285912666', '6000060285968865',
          '6000060285986006', '6000060286048091', '6000060286091596', '6000060286117523', '6000060286187430',
          '6000060286197465', '6000060286349444', '6000060286369920', '6000060286403660', '6000060286413551',
          '6000060286417968', '6000060286426949', '6000060286533431', '6000060286556059', '6000060286595864',
          '6000060286670372', '6000060286823653', '6000060286954351', '6000060286957811', '6000060286982865',
          '6000060287011733', '6000060287029653', '6000060287235449', '6000060287231096', '6000060287352204',
          '6000060287417868', '6000060287772938', '6000060287798974', '6000060287808918', '6000060287904635',
          '6000060287977744', '6000060288128045', '6000060288346997', '6000060288530136', '6000060288602727',
          '6000060288963837', '6000060289368328', '6000060289386415', '6000060289482294', '6000060289911927',
          '6000060290281302', '6000060290300265', '6000060290550360', '6000060290686839', '6000060291077380',
          '6000060291243806', '6000060291340862', '6000060291431540', '6000060291483681', '6000060291553294',
          '6000060291706959', '6000060292219430', '6000060292566439', '6000060292741605', '6000060293019252',
          '6000060293381519', '6000060293320112', '6000060293384730', '6000060293387871', '6000060293694236',
          '6000060293457750', '6000060293507340', '6000060293611888', '6000060293621190', '6000060295043630',
          '6000060295245128', '6000060295298124', '6000060295371605', '6000060295427413', '6000060295767894',
          '6000060295876437']
# usrids = ['6000060269448244', '6000060269448119', '6000060269652085']
import time
import requests
from lxml import html

browser = webdriver.Chrome()

browser.get("https://wealth.cloudpnr.com/p2padmin/")
input = browser.find_element_by_id("login_operator_id")
input.send_keys("mayanbin0302@163.com")
# input.send_keys(Keys.ENTER)

input = browser.find_element_by_id("login_password")
input.send_keys("972506")
# input.send_keys(Keys.ENTER)

str1 = input("Enter your input: ")

input = browser.find_element_by_id("captcha")
input.send_keys(str1)
input.send_keys(Keys.ENTER)
# 等待时间
wait = WebDriverWait(browser, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header-infos")))
# print(browser.current_url)
# print(browser.get_cookies())
# print(browser.page_source)
# time.sleep(10)


browser.get('https://wealth.cloudpnr.com/p2padmin/report/index/report/id/500005')

# tree = html.fromstring(browser.page_source)
# data = ''.join(tree.xpath('//span[contains(text(),"客户账户明细查询")]/text()'))

wait.until(EC.presence_of_element_located((By.CLASS_NAME, "main-content-title")))
# 点击查询
query = browser.find_element_by_xpath('//a[@class="btn btn-primary ajax-get-data"]')
# 查询开始时间
date_start_input = browser.find_element_by_name('date_from')
# 查询结束时间
date_end_input = browser.find_element_by_name('date_to')

# 客户号
cust_input = browser.find_element_by_name('custId')

for usrid in usrids:
    num = 0s
    cust_input.clear()
    cust_input.send_keys(usrid)

    queryDate = [['2018-03-12', '2018-06-10'], ['2018-06-11', '2018-07-31']]

    for dateq in queryDate:

        date_start_input.clear()
        date_start_input.send_keys(dateq[0])

        date_end_input.clear()
        date_end_input.send_keys(dateq[1])

        query.click()

        # "btn ajax-get-data btn-disabled"
        wait.until(EC.presence_of_element_located((By.XPATH, '//a[@class="btn ajax-get-data btn-primary"]')))

        # 获取总页数
        size = browser.find_element_by_xpath('//p[@class="page"]/span/strong').text
        # print(size)
        if int(size) > 0:

            # 数据总页数
            total = browser.find_element_by_xpath('//p[@class="page"]/input[@max]').get_attribute('max')
            for i in range(1, int(total) + 1):
                if i != 1:
                    next = browser.find_element_by_xpath('//p[@class="page"]/a[@title="Next"]')
                    next.click()
                wait.until(EC.presence_of_element_located(
                    (By.XPATH, '//p[@class="page"]/a[@class="current" and @title="' + str(i) + '"]')))
                # pageindex = browser.find_element_by_xpath('//div[@class="table dis"]/table/tbody/tr')

                trs = browser.find_elements_by_xpath('//div[@class="table dis"]/table/tbody/tr')
                for tr in trs:
                    one = list()
                    tds = tr.find_elements_by_xpath('.//td')
                    for j in range(0, len(tds)):
                        if j > 0:
                            one.append(tds[j].text)

                    insert(one)
                    # print(e.text)
                    num += 1
            # pageindex = browser.find_element_by_xpath('//p[@class="page"]/a[@class="current"]').text
            #     if i<total:

    print(usrid + ':' + str(num))

# print(browser.page_source)
browser.close()
# 关闭数据库连接
db.close()
