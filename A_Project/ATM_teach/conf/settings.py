# 存储配置文件
import os
import sys
import logging
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

DATABASE={
    'engine':'file_storage', #文件名
    'name':'accounts',  #数据库名
    'path':'%s/db'% BASE_DIR  #文件路径
}

LOG_LEVEL = logging.INFO
LOG_LEVEL = {
    'transaction':'transactions.log',
    'access': 'access.log',
}
TRANSACTION_TYPE = {
    'repay':{'action':'plus', 'interest':0},
    'withdraw':{'action':'minus', 'interest':0.05},
    'transfer':{'action':'minus', 'interest':0.05},
    'consume':{'action':'minus', 'interest':0},

}




























