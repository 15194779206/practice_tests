import requests


url = 'http://www.xiujukoo.com/upimg/allimg/161128/0618142.jpg'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) '}
html = requests.get(url, headers=headers).content
with open('赵丽颖.jpg', 'wb') as f:
    f.write(html)

