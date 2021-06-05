import pickle

# data={'k1':123,'k2':'hello'}
with open("test.text",'rb') as f:
    # datas=pickle.loads(f.read()) #和下面的内容一致
    datas=pickle.load(f)
    print(datas)