import requests

url = 'http://www.baidu.com'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
res= requests.get(url, headers=headers)
print(res.text)  #获取响应内容（字符串）
res.encoding = 'utf-8'
print(res.encoding)  #查看响应字符编码
#查看响应内容(bytes)
print(res.content)
#查看HTTP响应码
print(res.status_code)
#返回实际数据的URL地址
print(res.url)


