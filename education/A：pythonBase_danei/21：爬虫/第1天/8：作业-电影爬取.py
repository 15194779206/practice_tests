'''
爬取猫眼电影信息：猫眼电影-榜单-top100榜
第1步完成：
    猫眼电影-第1页.html
    猫眼电影-第2页.html
第2步完成
    ①提取数据：电影名称、主演、上映时间
    ②先打印输出，然后再写入到本地文件
'''
import urllib.request,urllib.parse,random

class MaoyanSpider():
    def __init__(self):
        self.baseUrl = 'https://maoyan.com/board/6?offset={}'
        self.agent = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}

    def get_page(self,urls):
        req = urllib.request.Request(url=urls,headers=self.agent)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')

        return html

    def parse_page(self):
        pass

    def write_page(self,name,html):
        with open(name,'w',encoding='utf-8') as f:
            f.write(html)


    def main(self):
        start = int(input("start:"))
        end = int(input("end:"))
        for page in range(start,end+1):
            filename = "猫眼电影-第{}页.html".format(page)
            pn = (start-1)*10
            url = self.baseUrl.format(pn)
            html = self.get_page(url)
            self.write_page(filename,html)



if __name__ =="__main__":
    spider = MaoyanSpider()
    spider.main()