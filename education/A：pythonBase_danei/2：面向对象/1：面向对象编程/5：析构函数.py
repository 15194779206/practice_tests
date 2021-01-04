class FileManage:
    def __init__(self,filename='a.text'):
        self.file=open(filename,'w',encoding='utf-8')

    def writeline(self,string):
        self.file.write(string)
        self.file.write('\n')
    def __del__(self):
        """析构方法会在对象销毁前自动调用"""
        self.file.close()
        print("文件已关闭")
fm=FileManage()
fm.writeline('hello world')
fm.writeline("这是第二行内容")
# print(fm.__class__) #<class '__main__.FileManage'>
