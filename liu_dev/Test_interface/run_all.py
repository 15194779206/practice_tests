import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from Test_interface.config.config import *

suit =unittest.defaultTestLoader.discover(test_case_path)
with open(report_file,'wb') as f:
    HTMLTestRunner(stream=f,title="股书接口测试",description="接口测试说明文档").run(suit)