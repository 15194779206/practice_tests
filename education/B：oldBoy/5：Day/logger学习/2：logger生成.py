import logging

#1.生成logger对象
logger =logging.getLogger("web")
logger.setLevel(logging.INFO) #设置日志级别
# 日志级别 debug() info() warning() error() critical()
#2.生成handler对象
ch=logging.StreamHandler()  #向谁输出信息
fh=logging.FileHandler('web.log')
#2.1.把handler对象绑定到logger对象
logger.addHandler(ch)
logger.addHandler(fh)
#3.生成formatter对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#3.1.把formatter对象绑定handler对象

ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)

#4.输出日志
logger.debug("test debug log")
logger.info("test info log")