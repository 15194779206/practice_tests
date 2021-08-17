import re
html= '''
<html>
    <div><p>第一条数据</p></div>
    <div><p>第二条数据</p></div>
</html>
'''

#贪婪匹配
pattern = re.compile('<div><p>.*</p></div>', re.S)
r_list = pattern.findall(html)
print('贪婪匹配',r_list)
#

#非贪婪匹配
pattern = re.compile('<div><p>(.*?)</p></div>', re.S)
r_list = pattern.findall(html)
print('非贪婪匹配', r_list)


#分组
s =  'A B C D'
test = re.findall('(\w+)\s+(\w+)', s)
print(test)

























