'''
描述：输入搜索内容，根据起始页和终止页进行打印，
'''
from urllib import request,parse
import random,time
class baiduSpider(object):
    def __init__(self):
        #http://tieba.baidu.com/f?kw=%E8%B5%B5%E4%B8%BD%E9%A2%96&ie=utf-8&pn=150
        self.url = "http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}"
        self.header = {"User-Agent": "User-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"}
    def get_page(self,url):  #获取页面
        req = request.Request(url,headers=self.header)
        res = request.urlopen(req)
        html = res.read().decode("utf-8")
        return html
    def write_page(self,filename,html):#保存数据
        with open(filename,"w",encoding="utf-8") as f:
            f.write(html)

    def main(self):
        name = input("请输入搜索内容：")
        start = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        for page in range(start,end):
            kw = parse.quote(name)
            pn = (page+1)*50
            URL = self.url.format(kw, pn)
            html = self.get_page(URL)
            filename = "{}-第{}页.html".format(name, page)
            self.write_page(filename,html)
            print("第%s页爬取成功"%page)
            time.sleep(random.randint(1,3))

if __name__ =="__main__":
    spider = baiduSpider()
    spider.main()

























