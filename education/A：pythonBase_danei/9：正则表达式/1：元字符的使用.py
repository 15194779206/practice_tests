import re

#1：普通字符
# re.findall(正则表达式,目标字符串)
test= re.findall('.ab', 'cabcedabc')
print(test)#['cab', 'dab']

#2：或  |
test = re.findall('com|cn','www.baidu.com.cn')
print(test) #['com', 'cn']

#3：匹配单个字符
test= re.findall('张.丰', '张三丰,张四丰,张小小')
print(test)#['张三丰', '张四丰']

#4：匹配字符集
test = re.findall('[0-9]', 'hel a-001')
print(test)#['0', '0', '1']
test= re.findall('[-0-9]', 'hel a-001')
print(test)#['-', '0', '0', '1']

# 5：匹配字符集反集
test = re.findall('[^-0-9]', 'hel a-001')
print(test)#['h', 'e', 'l', ' ', 'a']

# 6：匹配字符开始位置
test = re.findall('^jame', 'jame,hi')
print(test)#['jame']

# 7：匹配字符结尾位置
test = re.findall('jame$', 'hi,jame')
print(test)#['jame']

#8:使用技巧
test = re.findall('^jame$', 'jame')
print(test)#['jame']

#9：匹配字符重复
    #9.1*
test = re.findall('wo*', 'wooooo~w')
print(test)#['wooooo', 'w']

#匹配以大写字母开头的单词
test = re.findall('[A-Z][a-z]*', 'Hello word,Hi tom')
print(test)#['Hello', 'Hi']

    #9.2 +
test = re.findall('wo+', 'wooooo~w')
print(test)#['wooooo'  ]
    #9.3 ?
test = re.findall('wo?', 'wooooo~w')
print(test) #['wo', 'w']
test = re.findall('-?[0-9]+', 'Jame,age:18,-26,-213')
print(test) #['18', '-26', '-213']
test = re.findall('-?[0-9]+', '工资：1800，小刚：-500')
print(test) #['1800', '-500']
    #9.4 {n}
test = re.findall('1[0-9]{10}', '23455,15194779200')
print(test) #['15194779200']
    #9.4 {m,n}
test = re.findall('[0-9]{1,3}', '15194779200')
print(test) #['151', '947', '792', '00']

#10:匹配任意(非)数字字符
test = re.findall('\d{1,5}', 'Mysql:3306,http:8080')
print(test) #['3306', '8080']

test = re.findall('\D{1,5}', 'Mysql:3306,http:8080')
print(test) #['Mysql', ':', ',http', ':']

#匹配任意正数和负数
test = re.findall('-?\d+\.?\d*', '-23.8,4,20%,22.1%,-64,-23.5')
print(test)  #['-23.8', '4', '20', '22.1', '-64', '-23.5']

#10:匹配任意(非)普通字符
test = re.findall('\w+', 'server_port = 8888')
print(test) #['server_port', '8888']
test = re.findall('\W+', 'server_port = 8888')
print(test) #[' = ']

#11:匹配任意(非)空字符
test = re.findall('\w+\s+\w+', 'hello  word')
print(test) #['hello  word']

test = re.findall('\S+', 'Tedu-0.1~oo   xxxx')
print(test) #['Tedu-0.1~oo', 'xxxx']

#11:匹配开头结尾位置
test = re.findall('\Ah', 'hello  word')
print(test) #['h']
test = re.findall('\Zd', 'hello  word')
print(test) #[]

#11:匹配单词边界
test = re.findall(r'\b[A-Z]\w+', '1 This is iPython')
print(test) #['This']

#2.1  正则表达式的转义
test = re.findall('\$\d+', '薪资:$100')
print(test) #['$100']

test = re.findall(r'\d+', '薪资:$100')
print(test) #['100']

test = re.findall(r'\(.+\)', '(hello world),zha(Tom)')
print(test) #['(hello world),zha(Tom)']

#3.1正则表达式分组
test = re.search(r'(ab)*','ababababab').group()
print(test)
test = re.search(r'王|李\w{1,3}','王者荣耀').group()
print(test)#王
test = re.search(r'王|李\w{1,3}','李时珍').group()
print(test)#李时珍
test = re.search(r'(王|李)\w{1,3}', '王者荣耀').group()
print(test)#王者荣耀


#4.1捕获组

test = re.search(r'(?P<pig>)ab', 'abcdf').group()
print(test) #ab

