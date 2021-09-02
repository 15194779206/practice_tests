from Test_interface.lib.send_request import *
import re

def execute(case,cookie=None):
    res=send_request(case, cookie=cookie)
    checkinfo =None
    if re.search('<h4>A PHP Error was encountered</h4>', res.text):  #
        checkinfo = re.search('<h4>A PHP Error was encountered</h4>([\s\S]*)Line Number: (.*?)</p>', res.text).group(0)
        return [res, checkinfo]

    if re.search('<title>(.*?)</title>', res.text):
        # 通过正则表达式查找返回的数据中是否存在title标签，来判定返回的是否为网页
        checkinfo = re.search('<title>(.*?)</title>', res.text).group(1)
        # htmlTitle = res.text.split('<title>')[1].split('</title>')[0]
        # log_case_info(case, res, checkinfo)
        return [res, checkinfo]
    else:
        return [res, checkinfo]

