'''
1：输入一个字符串整数代表星期几（0-6），0代表周日，1代表周一
任意输入字符串，打印这个字符串是否代表星期几，如果不是以上字符打印“字典内没有相应的数据”
（要求将以上数据存在字典中，键为字符串中的一个，值为星期几或周几）
'''


days={'0':"星期日",'零':"星期日",
      '1':"星期一",'一':"星期一",
      '二':"星期二",'2':"星期二",
      '三':"星期三",'3':"星期三",
      '四':"星期四",'4':"星期四",
      '五':"星期五",'5':"星期五",
      '六':"星期六",'6':"星期六",
      }

while True:
    week = input("请输入数字：")
    if not  days:
        break
    if week in days:
        print(days[week])
    else:
        print('字典内没有相应的数据')

