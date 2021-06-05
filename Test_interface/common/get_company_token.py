import html5lib
from bs4 import BeautifulSoup
import requests
def company_token(text):
    company_dict = {}
    soup = BeautifulSoup(text, 'html.parser')
    nameList = soup.find_all(class_='enterpListName')
    tokenList = soup.find_all(class_="clickCompany")
    for i in range(len(nameList)):
        company_name = nameList[i].get('title').strip('')
        company_token = tokenList[i].get("data").strip('')
        company_dict[company_name] = company_token

    return company_dict






'''

Login_url ='https://test.kapbook.cn/login/check_login_ajax'
header= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
Login_data={'email': '15028217377','password': 'MTIzNDU2','type': '1'}
response = requests.post(url=Login_url,data=Login_data,headers=header)
times = response.cookies['request_time']
tokens=response.cookies['token']
cookie = {
    "request_time":times,
    "token":tokens,
}
company_url ="https://test.kapbook.cn/user/index?from=login"
company_text = requests.get(url=company_url,cookies=cookie, headers=header)
soup = BeautifulSoup(company_text.text, "html5lib")
nameList = soup.find_all(class_='enterpListName')  # 获取公司名称
# 不能用soup.find_all方法的原因是，当vie公司处于初始化状态时，class信息与正常公司的class信息不一致，导致无法正常获取
tokenList = soup.select('.enterpListTotal.enterpListMore.clickCompany')  # 获取data
print(nameList)

'''




