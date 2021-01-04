import urllib.request
import urllib.parse


#拼接url
baseurl = "http://www.baidu.com/s?wd="
key = input("请输入搜索内容：")
tedu = urllib.parse.quote(key)  #进行urlencode()编码
url = baseurl + key
print(url)
headers = {'User-Agent': "Mozilla/5.0"}
req = urllib.request.Request(url, headers=headers)  #创建请求对象
res = urllib.request.urlopen(req)  #获取响应对象
html = res.read().decode("utf-8")
with open("搜索.html", "w", encoding="utf-8") as f:
    f.write(html)
