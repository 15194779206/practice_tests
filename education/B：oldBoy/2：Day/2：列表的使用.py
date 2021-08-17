#列表的使用

name=["张三","李四","王五","赵六","屎蛋"]
de=["删除内容"]
#切片的使用
print(name[1])
print(name[0:3])  #顾头不顾尾
print(name[-1])  #选取倒数第一个
print(name[-2:-1])  #顾头不顾尾['赵六']
#追加，在后面追加
name.append("追内容")
print(name)
#插入，在第几个元素之前进行插入操作
name.insert(2,"插内容")
print(name)
#修改
name[2]="休内容"
print(name)
#删除内容
del name[1]
print(name)
#删除指定元素
name.remove("张三")
print(name)
name.pop() #删除最后一个元素
print(name)
#扩展，在后面添加
name2=[1,2,3]
name.extend(name2)
print(name)

