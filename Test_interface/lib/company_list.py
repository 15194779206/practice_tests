from bs4 import BeautifulSoup
from Test_interface.config.config import *
import requests

def get_text(time, token):
    cookie = {
        'request_time': time,
        'token': token
    }
    resp = requests.get(test_url + '/user/index?from=login', cookies=cookie)
    return resp


def company_list(time,token):
    companyList = []
    res= get_text(time,token)
    soup = BeautifulSoup(res.text, "html5lib")
    nameList = soup.find_all(class_='enterpListName') #获取公司名称
    # 不能用soup.find_all方法的原因是，当vie公司处于初始化状态时，class信息与正常公司的class信息不一致，导致无法正常获取
    tokenList = soup.select('.enterpListTotal.enterpListMore.clickCompany') #获取data
    typeList = soup.find_all(class_='enterpListRight fl')  #获取企业类型
    for i in range(len(nameList)):
        name = nameList[i].get('title').strip('')#获取公司名称
        token = tokenList[i].get('data') #获取company_token
        type = typeList[i].find_all('div')[1].find_all('span')[1].get_text().strip('') #获取类型
        finance = typeList[i].find_all('div')[2].find_all('span')[1].get_text().strip('') #获取轮次
        companyList.append({'name': name, 'token': token, 'type': type, 'finance': finance})
    # print(companyList)
    return companyList