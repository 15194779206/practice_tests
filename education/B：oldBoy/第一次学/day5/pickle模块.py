import pickle

data={'k1':123,'k2':'hello'}
#pickle.dumps将数据通过特殊的形式转换为只有python语言认识的字符串
p_str=pickle.dumps(data)
print(p_str)    #获取内存地址
#pickle.dump将输入通过特殊的形式转换为只有python语言认识的字符串，并写入文件
with open('pickle模块','w+')as f1:
    # print(f1.read())
    pickle.dump(data,f1)





