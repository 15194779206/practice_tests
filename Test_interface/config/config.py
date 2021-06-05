import logging
import os
import time


today=time.strftime('%Y-%m-%d',time.localtime())
now = time.strftime('%Y%m%d_%H%M', time.localtime())


#项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
test_case_path=os.path.join(prj_path,'test','case')#用例目录


report_file=os.path.join(prj_path,'report','report_{}.html'.format(now))



#测试地址
test_url = 'https://test.kapbook.cn'