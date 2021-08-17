data=[1,2]
# data[4]
try:
    data[4]
# except IndexError as e:
#     print("类型错误")
#抓住一个以上错误
except (IndexError,TypeError) as e:
    print("出错啦")

# 抓住所有的错误，一般放在最后，实在找不到错误报异常
# except Exception as e:
#     print("出错地方",e)
else: #如果不出错出现的提示信息
    print("一切正常")
finally:
    print("不管出不出错都执行")
