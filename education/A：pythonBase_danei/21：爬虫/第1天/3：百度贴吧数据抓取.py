# import urllib.parse
# import urllib.request
from  urllib import request,parse
import time,random

class BaiduSpider(object):
    def __init__(self):
        #https://www.baidu.com/s?wd=##&pn=0
        self.url = 'https://www.baidu.com/s?kw={}&pn={}'
        self.headers = {"User-Agent": "User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}

    #获取相应对象
    def get_page(self, urls):
        req = request.Request(url=urls, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode("utf-8")
        return html

    #提取数据
    def parse_page(self):
        pass

    #保存数据
    def write_page(self, filename, html):
        with open(filename, "w", encoding='utf-8') as f:
            f.write(html)

    def main(self):
        name = input("请输入贴吧名：")  # filename
        start = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        for page in range(start, end):
            pn = (page+1)*50
            kw = parse.quote(name)
            url = self.url.format(kw, pn)
            html = self.get_page(url)  #获取响应，并保存
            filename = "{}-第{}页.html".format(name, page)
            self.write_page(filename, html)
            print("第{}页爬取成功".format(page))
            time.sleep(random.randint(1, 3))

if __name__ == "__main__":
    spider = BaiduSpider()
    spider.main()