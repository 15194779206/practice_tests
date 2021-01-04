import urllib.request
import urllib.parse


#拼接url
baseurl = "http://httpbin.org/get"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"}
req = urllib.request.Request(baseurl, headers=headers)  #创建请求对象
res = urllib.request.urlopen(req)  #获取响应对象
html = res.read().decode("utf-8")
print(html)
