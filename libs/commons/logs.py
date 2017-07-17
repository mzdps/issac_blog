#!/usr/bin/env python
# -*-coding:utf-8-*-
'''
Author : issac
date   : 2017/7/13 下午5:06
role   : Version Update
'''

import logging

from libs.commons.common import singleton
from settings import settings


@singleton
class Logger(object):

    def __init__(self, log_name):
        self.__log_key = log_name
        self.__log_file = settings['blog_log_path']

    def get_logger(self):
        logger = logging.getLogger(self.__log_file)
        logger.setLevel(logging.INFO)  # Log等级总开关

        # 第二步，创建一个handler，用于写入日志文件
        fh = logging.FileHandler(self.__log_file, mode='a')
        fh.setLevel(logging.INFO)  # 输出到file的log等级的开关

        # 第三步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)  # 输出到console的log等级的开关

        # 第四步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s *-----* %(filename)s[line:%(lineno)d] *-----*"
                                      " %(funcName)s *-----* %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 第五步，将logger添加到handler里面
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

log = Logger('blog_log').get_logger()


if __name__ == '__main__':
    log.info('1233213')
    log.info('this ging info message')
    log.debug('this is a loggging debug message')
    log.warning('this is loggging a warning message')
    log.error('this is an loggging error message')
    log.critical('this is a loggging critical message')
