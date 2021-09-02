import unittest
from HTMLTestRunner import HTMLTestRunner
from conf.conf import *
# from lib.sendmail import send_email

logging.info("=============================================== 测试开始 ===============================================\n")
suite = unittest.defaultTestLoader.discover(test_case_path)  # 从配置文件中读取用例路径

with open(report_file, 'wb') as f:  # 从配置文件中读取
    HTMLTestRunner(stream=f, title="股书Web UI自动化测试", description="本报告用于描述股书SaaS的Web UI测试情况说明").run(suite)

# send_email(report_file)  # 从配置文件中读取
logging.info("=============================================== 测试结束 ===============================================\n\n")
