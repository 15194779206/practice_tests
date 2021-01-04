import urllib.request
import urllib.parse

#拼接url
#https://www.baidu.com/s?ie=UTF-8&wd=%E7%BE%8E%E5%A5%B3
key = input("请输入搜索内容：")
baseurl = "https://www.baidu.com/s?ie=UTF-8&"
headers = {'User-Agent': "Mozilla/5.0"}
tedu = urllib.parse.urlencode({"wd": key})  #进行urlencode()编码 #或wd = {"wd": "美女",}
url = baseurl + tedu
req = urllib.request.Request(url, headers=headers)  #创建请求对象
res = urllib.request.urlopen(req)  #获取响应对象
html = res.read().decode("utf-8") #获取响应内容
# print(html)
filename = '{}.html'.format(key)
with open(filename, "w", encoding="utf-8") as f:
    f.write(html)
