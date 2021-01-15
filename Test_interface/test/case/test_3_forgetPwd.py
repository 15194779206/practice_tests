import requests
from Test_interface.lib.header_choose import *
forgetPwd_ulr = 'https://test.kapbook.cn/resetpwd/set_login_pwd_ajax'

datas ={
    'email':'15194779206',
    'verify_code': '414628',
    'password': 'MTIzNDU2',
    'nationcode_id': '214',
    'nationcode': '86',
}

# cookies ={
#     'resetpwd_email_check':'e5275c8b81e814a36fc16af294141040'
# }

res= requests.post(url=forgetPwd_ulr, data=datas, headers=headers_choose())
print(res.json())