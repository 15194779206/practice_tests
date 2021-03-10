from Test_interface.lib.company_list import *
from Test_interface.common.get_company_token import *
from Test_interface.config.config import *
from Test_interface.lib.random_num import *
from Test_interface.lib.header_choose import *
import requests

def enter_company(time,token):
    # keys = get_text(time,token)
    keyList=[]
    company_dict =company_list(time,token)
    total = len(company_dict)
    for key in company_dict:
        keyList.append(key['token'])
    num =random_num(total)
    special_token=keyList[num]
    return special_token
    # cookie = {
    #     "request_time":time,
    #     "token":token,
    #     "company_token":special_token
    # }
    # url=test_url + '/equity/certificate_list'
    # tests=requests.get(url=url, cookies=cookie, headers=headers_choose())
    # return tests.text



#测试代码
# token= get_token_admin()
# enter_company(token['request_time'],token['token'])

