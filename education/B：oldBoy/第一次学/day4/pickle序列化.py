__author__ = "Alex Li"
#import json
import pickle

def sayhi(name):
    print("hello,",name)

info = {
    'name':'alex',
    'age':22,
    'func':sayhi
}


f = open("test.text","wb")
#print(json.dumps(info))
print( )
#
f.write( pickle.dumps( info) )
# 另一种写法,和上面的一样
# pickle.dump(info,f)
f.close()