#!usr/bin/env python
#-*- coding:utf-8 -*-

from practice_P2P.tools import project_path
import pandas as pd
class GetData:
    Cookie = None
    loan_id = None
    Telphone = pd.read_excel(project_path.test_data_path,sheet_name='init').ix[0,0]
    normal_tel = pd.read_excel(project_path.test_data_path,sheet_name='init').ix[1,0]
    admin_tel = pd.read_excel(project_path.test_data_path,sheet_name='init').ix[2,0]
    # loan_member_id = pd.read_excel(project_path.test_data_path,sheet_name='init').ix[3,0]
    pwd = '666666'

# setattr(GetCookie,'Cookie','12345')     #设置属性值
# print(getattr(GetCookie,'Cookie'))      #获取属性值
# print(hasattr(GetCookie,'Cookie'))      #判断是否存在该属性
# delattr(GetCookie,'Cookie')             #删除该属性
# print(hasattr(GetCookie,'Cookie'))
data = GetData().normal_tel
print(data)
