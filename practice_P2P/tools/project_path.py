#!usr/bin/env python
#-*- coding:utf-8 -*-
import os

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#测试用例的路径
test_data_path = os.path.join(project_path,'test_data','test_data.xlsx')
# print(test_data_path)
#测试报告的路径
test_report_path = os.path.join(project_path,'test_result','html_report','test_api.html')
# print(test_report_path)
#配置文件的路径
test_config_path = os.path.join(project_path,'conf','case.config')
# print(test_config_path)
#日志报告文件的路径
log_path = os.path.join(project_path,'test_result','log','log.txt')