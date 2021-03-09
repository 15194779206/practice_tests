from Test_interface.lib.company_list import *
from Test_interface.common.get_company_token import *
from Test_interface.config.config import *
from Test_interface.lib.random_num import *
import requests

def enter_company(time,token):

    text = get_text(time,token)
    keyList=[]
    company_dict=company_token(text)
    total =len(company_dict.keys())
    for key in company_dict.keys():
        keyList.append(key)
    num = random_num(total)
    special_token =company_dict[keyList[num]]
    head = {
        'cookie': 'request_time=' + time + ';' + 'token=' + token + ';' + 'company_token=' + special_token
    }
    requests.get(test_url + '/equity/certificate_list', headers=head)
    return special_token



# Login_url ='https://test.kapbook.cn/login/check_login_ajax'
# header= {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# Login_data={'email': '15028217377','password': 'MTIzNDU2','type': '1'}
# response = requests.post(url=Login_url,data=Login_data,headers=header)
# time = response.cookies['request_time']
# token=response.cookies['token']
# lists = enter_company(time,token)
# print(lists)