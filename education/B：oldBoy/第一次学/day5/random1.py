import random

print(random.random())
print(random.uniform(0,3))
print(random.randint(1,9))
print(random.randrange(0,9,2))
print(random.choice("unlic"))
print(random.sample('abcdef',3))  #结果['b', 'c', 'e']
# 洗牌
items=[1,2,3,4,5,6,7]
random.shuffle(items)
print(items)