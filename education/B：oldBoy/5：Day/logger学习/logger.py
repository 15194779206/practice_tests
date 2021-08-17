import logging

logging.basicConfig(filename='log_test.log',
                    level=logging.DEBUG,  #debug级别最低，在他之上的界别都可进行打印
                    #不管前面几位怎么样，后面需要有一个是空格的
                    format='%(asctime)s %(message)s',
                    datefmt='%Y-%m-%d  %I:%M:%S %p')
def sayhi():
    logging.error("from sayhi...")
sayhi()

logging.debug('debug is inp')
logging.info('info is inp')
logging.warning('warning is inp')
logging.error('error is inp')
logging.critical('critical is inp')
