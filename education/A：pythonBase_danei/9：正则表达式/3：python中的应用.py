import re

s = "Levi:1994 ,Sunny :1993"
pattern = r"(\w+):(\d+)"

#
regex = re.compile(r'abcdef')
print(regex.pattern)  #abcdef


#re模块调用
l = re.findall(pattern, s)
print(l) #[('Levi', '1994')]

#compile对象调用
regex = re.compile(pattern)
l = regex.findall(s)
print(l)  #[('Levi', '199')]

#split分隔
s = "hello world how are you L-boby"
test = re.split(r'[^\w]+', s) #以非普通字符进行分割
print(test)  #['hello', 'world', 'how', 'are', 'you', 'L', 'boby']


#sub
s = "时间：2019/10/12" #将/替换成-
test = re.sub('/', '-', s)
print(test) #时间：2019-10-12

#finditer
s = "2019年,建国70周年"
pattern = r"\d+"
it = re.finditer(pattern, s)
for i in it:
    print(i.group())  #2019   70

#fullmatch
m = re.fullmatch(r'[0-9a-zA-Z]+', "hello1973")
print(m.group())  #hello1973

#match
m = re.match(r'[A-Z]\w*' , "Hello world")
print(m.group())  #Hello

#search
m = re.search('\S+', "好\n嗨哟")
print(m.group()) #好











