skills=[{'id':1,"cool":100,'name':'zs'},{'id':2,"cool":102,'name':'ls'}]
def funall(target,changes):
    for item in target:
        if changes(item):  #是判断条件，也是变化点，可以提取
            yield  item


#封装变化点,函数式编程
def change01(item):
    return item['id'] ==1
for item in funall(skills,change01):
    print(item['id'],item['name']) #1 zs

#使用lambda表达式可以写成
for item in funall(skills,lambda item:item['id'] ==1):
    print(item['id'],item['name']) #1 zs

lists = funall(skills,change01)
print(next(lists))    #{'id': 1, 'cool': 100, 'name': 'zs'}

