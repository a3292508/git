#!usr/bin/env python
#-*- coding:utf-8 -*-

import logging
from practice_P2P.tools.project_path import log_path

class MyLog:
    """日志类的封装"""
    def my_log(self,msg,level):

        # 定义一个日志收集器,名称可自定义
        my_logger = logging.getLogger('python11')

        # 设定级别
        my_logger.setLevel('DEBUG')

        # 设置输出格式
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        # 指定输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel('DEBUG')  # 设定级别
        ch.setFormatter(formatter)

        # 指定输出到文件
        fh = logging.FileHandler(log_path, encoding='utf-8')
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        # 两者对接--指定输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        #收集日志
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        elif level == 'CRITICAL':
            my_logger.critical(msg)

        #关闭渠道
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_log(msg,'DEBUG')

    def info(self,msg):
        self.my_log(msg,'INFO')

    def warning(self,msg):
        self.my_log(msg,'WARNING')

    def error(self,msg):
        self.my_log(msg,'ERROR')

    def critical(self,msg):
        self.my_log(msg,'CRITICAL')

if __name__ == '__main__':
    MyLog().debug('这是一个。。。')