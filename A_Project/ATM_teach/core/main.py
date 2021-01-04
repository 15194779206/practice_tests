#主逻辑交互程序

import auth
import logger


#作用于全局的临时数据，验证登录状态
user_data={
    'account_id': None,  #账户id
    'is_authenticated': False,  #登录状态
    'account_data': None  #账户数据
}


def run():
    '''
    此模块用于验证用户是否登录
    '''
    acc_data=auth.acc_login(user_data, access_logger)
    if user_data['is_authenticated']:
        pass

























