#示例：
s='Beijing is capital'
L=s.split(' ')
print(L) #['Beijing', 'is', 'capital']

list=["C:","Name","User"]
z='//'.join(list)
print(z)  #C://Name//User

#练习
#有字符串“hello”，生成‘h e l l o "和’h-e-l-l-o'(用交互模式)
z=' '.join('hello')
print(z)
x='-'.join('hello')
print(x)