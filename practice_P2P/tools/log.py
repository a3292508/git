#!usr/bin/env python
#-*- coding:utf-8 -*-

#logging--是python自带的一个日志模块
#它的主要作用有两个：
#1.代替print方法，可以把大部分想要进行调试的信息打印出来或者输出到指定文件
#2.可以对一些输出的调试信息分类做输出，比如：
#DEBUG/INFO/WARNING/ERROR/CRITICAL（越往后级别越高，常用的是INFO和ERROR）

import logging

#logger:收集日志，debug/info/error（默认返回root，日志收集器的名字）
#handdler:输出日志的渠道，指定的文件 还是控制台

# logging.debug('今天是个好日子')
# logging.info('化龙ing')
# logging.warning('aixinxin')
# logging.error('hahaha')
# logging.critical('eeeeee')

#定义一个日志收集器
my_logger = logging.getLogger('python11')
#设定级别
# my_logger.setLevel('DEBUG')

#设置输出格式
formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

#指定输出到控制台
ch = logging.StreamHandler()
ch.setLevel('DEBUG')        #设定级别
ch.setFormatter(formatter)
#指定输出到文件
fh = logging.FileHandler('py11.txt',encoding='utf-8')
fh.setLevel('INFO')
fh.setFormatter(formatter)
#两者对接--指定输出渠道
my_logger.addHandler(ch)
my_logger.addHandler(fh)


#收集日志
my_logger.debug('yi')
my_logger.info('er')
my_logger.warning('san')
my_logger.error('si')
my_logger.critical('wu')