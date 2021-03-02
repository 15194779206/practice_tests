from Test_interface.lib.send_request import *
import re

def execute(case,cookie=None):
    res=send_request(case, cookie=cookie)
    checkinfo =None
    if re.search('<h4>A PHP Error was encountered</h4>', res.text):  #
        checkinfo = re.search('<h4>A PHP Error was encountered</h4>([\s\S]*)Line Number: (.*?)</p>', res.text).group(0)
        return [res, checkinfo]
    else:
        return [res, checkinfo]

