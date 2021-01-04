#集合：集合是无序的，天生去重，可进行关系测试
s=set()   #s为空集合
s={2,3,5,7}
s=set("ABC")
print(s)  #{'A', 'C', 'B'}
# s=set({1:'name',2:'age',3:'hobby'})
# print(s)  #{1, 2, 3}  取其键，不取值
# s=set('hello')
# print(s)  #{'l', 'h', 'o', 'e'} 天生去重
# s=set([1,2,3],'abc')   #错误的，含有列表，可变
# print(s)