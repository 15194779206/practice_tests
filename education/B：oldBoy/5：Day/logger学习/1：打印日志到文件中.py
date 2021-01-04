import  logging

logging.basicConfig(filename='one.text',
                    level=logging.DEBUG,
                    format='%(asctime)s-%(message)s-%(filename)s',  #打印内容模块
                    datefmt='%Y-%d-%m %I-%M-%S-%p')    #打印格式，固定，不修改
logging.debug("debug input")
logging.error("error input")
logging.warning("warning input")