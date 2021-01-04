'''
爬取猫眼电影信息：猫眼电影-榜单-top100榜
第一步完成：
    第XX页爬取完成
第2步完成
    ①提取数据：电影名称、主演、上映时间
    ②先打印输出，然后再写入到本地文件
'''
import urllib.request
import urllib.parse
import random, time, re
import csv

#https://maoyan.com/board/4?offset=0
class SpiderMaoyan(object):
    def __init__(self):
        self.url="https://maoyan.com/board/4?offset={}"
        # self.headers = {"User-Agent": "User-Agent:Mozilla/5.0"}
        self.ua_list=[
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)'
        ]
        self.page = 1
    def get_page(self, url):
        #每次使用随机的user-agent
        # for user_agent in self.ua_list:
        user_agent = {'User-Agent': random.choice(self.ua_list)}
        res = urllib.request.Request(url, headers=user_agent)
        req = urllib.request.urlopen(res)
        html = req.read().decode("utf-8")
        #调用解析函数
        self.parse_page(html)

    def parse_page(self, html):#解析模块
        pattern = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        r_list = pattern.findall(html)  #列表
        self.write_page(r_list)
    #打印
    # def write_page(self, r_list):
        # film_dict = {}
        # for rt in r_list:
        #     film_dict['name'] = rt[0].strip()
        #     film_dict['start'] = rt[1].strip()
        #     film_dict['time'] = rt[2].strip()[5:15]  #原数据为'上映时间：1998-11-13'切割数据
        #     print(film_dict)

    #保存在csv文件
    def write_page(self, r_list):
        with open('maoyan.csv','a') as f:  # 初始化写入文件
            for rt in r_list:
                writer = csv.writer(f)
                writer.writerow([rt[0], rt[1].strip(), rt[2].strip()[5:15]])

    def main(self):
        for offset in range(0, 21, 10):
            url = self.url.format(offset)
            self.get_page(url)
            time.sleep(random.randint(1, 3))
            print("第%d页爬取完成"%self.page)
            self.page+=1

if __name__ == '__main__':
    start = time.time()
    movie = SpiderMaoyan()
    movie.main()
    end = time.time()
    print('执行时间：%.2f'%(end-start))














