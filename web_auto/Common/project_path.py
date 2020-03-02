#!usr/bin/env python
#-*- coding:utf-8 -*-

import os
"""
项目各目录的路径
"""

#当前项目的根目录
project_dir = os.path.dirname(os.path.dirname(__file__))
#测试用例的目录路径
cases_dir = os.path.join(project_dir,'TestCases')
#测试数据的目录路径
datas_dir = os.path.join(project_dir,'TestDatas')
#日志的目录路径
log_dir = os.path.join(project_dir,'Result/log')
#测试报告的目录路径
report_dir = os.path.join(project_dir,'Result/report/')
#报错截图的目录路径
screenshot_dir = os.path.join(project_dir,'Result/screenshot/')