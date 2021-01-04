leader={"曹操","刘备","周瑜"}   #经理
emlpey={"曹操","周瑜","张飞","赵云"}  #技术员
"""
用集合求：
  1.即是经理也是技术员的有谁？
  2.是经理，但不是技术员的有谁？
  3.是技术员，但不是经理的有谁？
  4.张飞是经理吗？
  5.身兼一职的人都有谁？
  6.经理和技术员都有几个人？
"""
print('1题:',leader&emlpey)
print('2题:',leader-emlpey)
print('3题:',emlpey-leader)
jiao="张飞" in  leader
if jiao==False:
    print("张飞不在领导列表")
else:
    print("张飞存在领导列表中")

print('5题:',leader^emlpey)   #对称补集
print('6题:','领导：',len(leader),'员工:',len(emlpey))