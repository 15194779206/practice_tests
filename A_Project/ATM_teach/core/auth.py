import os
from core import db_handler
from conf import settings
from core import logger
import json
import time

def login_required(func):  #验证用户是否登录
    def wrapper(*args, **kwargs):
        if args[0].get('is_authenticated'):
            return func(*args, **kwargs)
        else:
            exit("user is not authenticated")
    return wrapper

def acc_auth2(account,password):
    db_api = db_handler.db_handler()
    

#此处用于验证登录模块，此处用于验证用户名和密码
def acc_login(user_data,log_obj):
    retry_count=0
    while user_data['is_authenticated'] is not True and retry_count <3:
        account=input("用户名：").strip()
        password=input("密码：").strip()
        auth=acc_auth2(account,password)   #此处用于判断登录过期
        if auth:
            user_data['is_authenticated'] = True
            user_data['account_id'] = account
            print('auth值', auth)
            return auth
        retry_count +=1
    else:
        log_obj.error("%s 验证码错误次数太多，强制退出" %account)
        exit()

