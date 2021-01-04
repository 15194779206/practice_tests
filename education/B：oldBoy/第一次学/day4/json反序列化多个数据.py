import json
__author__ = "Alex Li"
import json

f = open("test1.text","r")
#data = json.loads(f.read()) #data = pickle.loads(f.read())
for line in f:
    print(json.loads(line))

#     可以down好多次，但是只能load一次



