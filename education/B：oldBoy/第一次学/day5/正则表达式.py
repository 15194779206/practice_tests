import re

res=re.match("chen\d+","chen12rong123ha1234")
print(res.group())   #结果chen12
#'?'     匹配前一个字符1次或0次
re1=re.search('a?','alex')
print(re1) #结果a
re1=re.search('aaa?','alexaaa')
print(re1) #结果aaa
re1=re.search('aaa?','aalexaaa')
print(re1) #结果aa

#findall
re2=re.findall("[0-9]{1,3}","aa1bb23ccc7712233")
print(re2)  #['1', '23', '771', '223', '3']

#splitall
re3=re.split("[0-9]","abc12de123f4")
print(re3)  #结果['abc', '', 'de', '', '', 'f', '']

#sub
re4=re.sub("[0-9]+","9","12ab34cc")
print(re4)  #结果99ab99cc