#!usr/bin/env python
#-*- coding:utf-8 -*-

from practice_P2P.tools import project_path
import pandas as pd
class GetData:
    Cookie = None
    Telphone = pd.read_excel(project_path.test_data_path,sheet_name='init').ix[0,0]

# setattr(GetCookie,'Cookie','12345')     #设置属性值
# print(getattr(GetCookie,'Cookie'))      #获取属性值
# print(hasattr(GetCookie,'Cookie'))      #判断是否存在该属性
# delattr(GetCookie,'Cookie')             #删除该属性
# print(hasattr(GetCookie,'Cookie'))
