#!usr/bin/env python
#-*- coding:utf-8 -*-

import os
import configparser
from interface_auto.common.project_path import config_path
#拼接配置文件的路径
config_path = os.path.join(config_path,'config.ini')

class ReadConfig:
    """封装读取和写入配置文件的方法"""
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(config_path, encoding='utf-8')

    def read_config(self,option,section):
        """读取配置文件"""
        return self.conf[option][section]

    def write_data(self,option,section,value):
        """写入配置文件"""
        self.conf.set(option,section,value)
        self.conf.write(open(config_path,'w',encoding='utf-8'))

if __name__ == '__main__':
    data = eval(ReadConfig().read_config('DB','port'))
    print(data)
    ReadConfig().write_data('TIME','year','hoss_new_20141016_bak99')