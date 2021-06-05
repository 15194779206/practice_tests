#爬取非结构化数据
import requests

url="http://pic25.nipic.com/20121205/10197997_003647426000_2.jpg"
headers ={ "User-Agent":"Mozilla/5.0"}

res=requests.get(url,headers=headers)
html = res.content

with open("图片.jpg","wb") as f :
    f.write(html)

print("图片下载成功")