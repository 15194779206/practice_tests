import re
#打印出动物名称和动物信息
html= '''
<html>
    <div class="animal">
        <p class="name">
            <a title="Tiger"></a>
        </p>
        <p class="content">
            first content first content
        </p>
    </div>
    <div class="animal">
        <p class="name">
            <a title="Rabbit"></a>
        </p>
        <p class="content">
            second content second content
        </p>
    </div>
</html>
'''

pattern = re.compile('<div class="animal">.*?title="(.*?)".*?class="content">(.*?)</p>', re.S)
r_list = pattern.findall(html)
for rt in r_list:
    print("动物名称：", rt[0])
    print("动物信息：", rt[1].strip())
    print("*"*50)


#爬虫中字符串常用方法
print('hello word'.split())#['hello', 'word'] 分割
print('hello word'.strip())#hello word 去掉空格
print('hello word'.replace(' ', '#'))#hello#word   以什么进行分割
