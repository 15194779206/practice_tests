import requests
from Test_interface.lib.header_choose import *
from Test_interface.config.config import *

def get_token_admin():
    Login_url =test_url+'/login/check_login_ajax'
    Login_data={
        'email': '15028217377',
        'password': 'MTIzNDU2',
        'type': '1'
    }
    response = requests.post(url=Login_url,data=Login_data,headers=headers_choose)
    return response.cookies

def get_token_emplpyee():
    Login_url =test_url+'/login/check_login_ajax'
    Login_data={
        'email': 'lyangluck@126.com',
        'password': 'MTIzNDU2',
        'type': '1'
    }
    response = requests.post(url=Login_url,data=Login_data,headers=headers_choose)
    return response.cookies


