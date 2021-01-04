from lxml import etree

html='''
<html>
    <div class="animal">
        <p class="name">name中的内容1</p>
        <p class="content">
            first content first content
        </p>
    </div>
    <div class="animal">
        <p class="name">name中的内容2</p>
        <p class="content">
            second content second content
        </p>
    </div>
</html>
'''
parse_html = etree.HTML(html)
r_list = parse_html.xpath('//p[@class="name"]/text()')
print(r_list)

