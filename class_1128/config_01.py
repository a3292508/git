#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

#配置文件
#properties/config/ini/log4j,都是配置文件

#configparser模块:读取配置信息
import configparser
#section([MODE])  option=value(mode=all)

cf = configparser.ConfigParser()
cf.read('case.config',encoding='utf-8')     #如果有中文，需要用encoding,否则会出现乱码

#读取配置文件的数据
#打印标签中键的值
# res_1 = cf.get('MODE','mode')
# print(res_1)
#
# res_2 = cf['MODE']['mode']
# print(res_2)
#
# #打印所有的标签
# print(cf.sections())
# #打印所有的键值对
# print(cf.items('PYTHON'))

#数据类型
#配置文件里的数据都是字符串--->需要要用eval()方法转换一下数据类型
print(type(cf.get('MODE','mode')))
print(type(cf.get('PYTHON','name')))