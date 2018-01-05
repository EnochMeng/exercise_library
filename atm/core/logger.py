##loger

import os,logging,sys

dir_atm=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,dir_atm)

from conf import settings

def logger(log_type):

    logging.basicConfig(level=settings.LOG_LEVEL,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        ##filename='',
                        ##filemode='',
                        )

    logger=logging.getLogger(log_type)
    
##    logger.setLevel(settings.LOG_LEVEL)

    ch=logging.StreamHandler()

##    ch.setLevel(settings.LOG_LEVEL)

    log_file=os.path.join(settings.BASE_DIR,r'\log')
    print(log_file)
    fh=logging.FileHandler(log_file)

##    fh.setLevel(settings.LOG_LEVEL)

##    formatter=logging.Formatter()

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger
