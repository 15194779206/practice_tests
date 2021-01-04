import pickle

data={'k1':123,'k2':'hello'}
f=open("test.text",'wb')
# f.write(pickle.dumps(data))  #和下面的写入方法是一样的
pickle.dump(data,f)
