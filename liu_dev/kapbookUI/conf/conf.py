import logging
import os
import time

today = time.strftime('%Y%m%d', time.localtime())
now = time.strftime('%Y%m%d_%H%M', time.localtime())

prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级的上一级目录（增加一级）
log_file = os.path.join(prj_path, 'log', 'log_{}.txt'.format(today))  # 更改路径到log目录下
data_file = os.path.join(prj_path, 'data', 'test_data.xlsx')
test_case_path = os.path.join(prj_path, 'test')   # 用例目录
report_file = os.path.join(prj_path, 'report', 'REPORT_{}.html'.format(now))  # 更改路径到report目录下

# 测试环境
test_env = 'https://test.kapbook.cn'
# test_env = 'https://demo.kapbook.com'
# test_env = 'https://web.kapbook.com'
reset = '/resetpwd'
register = '/register'
user = '/user'
certificate_list = 'equity/certificate_list'   #证书添加
Participants_add = '/company/people/index'  #公司管理
holdPlatform = '/company/hold_platform/index' #持股平台

# log配置
logging.basicConfig(level=logging.INFO,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式