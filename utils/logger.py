import logging
import os
if not os.path.exists('logs'):
    os.makedirs('logs')
def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    #文件输出
    file_handler = logging.FileHandler('logs/test.log',encoding = 'utf-8')
    file_handler.setLevel(logging.INFO)

    #控制台输出
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
logger = setup_logger()