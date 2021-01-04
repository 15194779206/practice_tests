import pickle
# 函数序列化
def sayhi(name):
    print("hello2,",name)

f = open("test.text","rb")

data = pickle.loads(f.read())
# 另一种写法，和上面的一致
# data=pickle.load(f)
print(data)