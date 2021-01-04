import requests

url ="http://www.baidu.com"
headers ={ "User-Agent":"Mozilla/5.0"}
respone =requests .get(url,headers =headers)  #发请求获响应
# print(respone.text)  #获取响应对象内容
print(respone.encoding)    #默认返回编码格式   ISO-8859-1
respone.encoding="utf-8"  #设置返回编码格式
print(type(respone.text))     #获取字节流    <class 'str'>
print(type(respone.content))     #获取字节流  <class 'bytes'>
print(respone.status_code)
print(respone.url)





















