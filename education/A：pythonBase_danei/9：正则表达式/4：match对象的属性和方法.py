import re

pattern = r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
#获取match对象
obj = regex.search('abcdefghi')
print(obj.pos) #目标字符串开头位置  0
print(obj.endpos)   #9
print(obj.re) #re.compile('(ab)cd(?P<pig>ef)')

#属性方法

print(obj.start())  #0
print(obj.end()) #6
print(obj.span()) #(0,6)
