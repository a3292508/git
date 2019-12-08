#!usr/bin/env python
#-*- coding:utf-8 -*-
import os

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

test_data_path = os.path.join(project_path,'test_data','test_data.xlsx')
print(test_data_path)
test_report_path = os.path.join(project_path,'test_result','html_report','test_api.html')
print(test_report_path)