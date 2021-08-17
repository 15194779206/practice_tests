import xml.etree.ElementTree as ET

tree = ET.parse("xml_test.xml")   #xmltest.xml为xml的文档
root = tree.getroot()    #获取所有内容
print(root.tag)   #获取文件的头标题

#1：遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
        print(i.tag,i.text)

#2：只遍历year 节点
for node in root.iter('year'):
    print(node.tag,node.text)

#3：修改
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated","yes")    #此处给year添加属性
tree.write("xmltest.xml")

#4：删除node
for country in root.findall('country'):
   rank = int(country.find('rank').text)
   if rank > 50:
     root.remove(country)

tree.write('output.xml')

