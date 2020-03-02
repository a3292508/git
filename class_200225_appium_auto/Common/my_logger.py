#!usr/bin/env python
#-*- coding:utf-8 -*-

import logging
import os
from class_200225_appium_auto.Common.project_path import log_dir

#指定日志文件的路径
file_path = os.path.join(log_dir,'log.txt')

class MyLogger:
    """封装打印日志操作"""
    def create_logger(self,message,level):
        my_logger = logging.getLogger('appium_auto')       #定义一个日志收集器
        my_logger.setLevel('DEBUG')                     #设定日志的级别
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')       #设定输出格式
        #指定输出到控制台
        control_handler = logging.StreamHandler()
        control_handler.setLevel('ERROR')
        control_handler.setFormatter(formatter)
        my_logger.addHandler(control_handler)

        #指定输出到文件
        file_handler = logging.FileHandler(file_path,encoding='utf-8')
        file_handler.setLevel('DEBUG')
        file_handler.setFormatter(formatter)
        my_logger.addHandler(file_handler)

        #根据级别收集日志
        if level == 'DEBUG':
            my_logger.debug(message)
        elif level == 'INFO':
            my_logger.info(message)
        elif level == 'WARNING':
            my_logger.warning(message)
        elif level == 'ERROR':
            my_logger.error(message)
        elif level == 'CRITICAL':
            my_logger.critical(message)

        #关闭渠道
        my_logger.removeHandler(control_handler)
        my_logger.removeHandler(file_handler)

    def debug(self,message):
        self.create_logger(message,'DEBUG')

    def info(self,message):
        self.create_logger(message,'INFO')

    def warning(self,message):
        self.create_logger(message,'WARNING')

    def error(self,message):
        self.create_logger(message,'ERROR')

    def critical(self,message):
        self.create_logger(message,'CRITICAL')

if __name__ == '__main__':
    MyLogger().debug('testing....')
    MyLogger().error('erroring...')