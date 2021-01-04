az=""
start=ord('A')
end=ord('Z')
while start<=end:
    az+=chr(start)  #生成大写
    az+=chr(start+0x20)  #生成小写
    start+=1
else:
    print(az)
