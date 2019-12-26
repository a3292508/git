#!usr/bin/env python
#-*- coding:utf-8 -*-

import os
"""
该模块用来存放整个项目目录的路径
"""

#当前项目目录的路径
project_path = os.path.dirname(os.path.dirname(__file__))

#配置文件的目录路径
config_path = os.path.join(project_path,'conf')
#测试用例的目录路径
cases_path = os.path.join(project_path,'test_cases')
#测试数据的目录路径
data_path = os.path.join(project_path,'test_data')
#测试日志的目录路径
log_path = os.path.join(project_path,'test_log')
#测试报告的目录路径
report_path = os.path.join(project_path,'test_reports')
