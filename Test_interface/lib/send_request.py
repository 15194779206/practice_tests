import json
import requests
from Test_interface.lib.pwd_base64 import *
from Test_interface.config.config import *
from Test_interface.lib.header_choose import *


def send_request(case,cookie=None):
    if cookie is None:
        cookies =None
    else:
        cookies = json.loads(case.get("cookies"))
        #进入公司cookie需带入company_token,此处进行判断
        if cookies['request_time']:
            cookies['request_time'] = cookie['request_time']
        if cookies['token']:
            cookies['token'] = cookie['token']
        if 'company_token' in cookie:
            if cookies['company_token']:
                cookies['company_token'] = cookie['company_token']

    if case.get('data'):
        data = json.loads(case.get('data'))
        try:
            if data['password']:
                data = base64Encode(data)
        except:
            pass
    else:
        data =None

    url = case.get('url')
    realurl =test_url+url
    method = case.get('method')
    try:
        if method == "POST":
            res = requests.post(url=realurl, cookies=cookies, data=data, headers=headers_choose())
        else:
            res = requests.get(url=realurl,cookies=cookies, params=data, headres=headers_choose())
    except Exception as e:
        return "请求失败"
    return res































