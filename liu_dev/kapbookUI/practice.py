import requests

response = requests.get('https://www.baidu.com/')
print(response.text)
print(response.status_code)
print(response.cookies)