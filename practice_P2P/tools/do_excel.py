#!usr/bin/env python
#-*- coding:utf-8 -*-

import os
from openpyxl import load_workbook

class DoExcel:
    """操作excel文件"""

    # @staticmethod     #可以设置成静态函数
    def get_data(self,file_name,sheet_name):
        """获取数据"""
        wb = load_workbook(file_name)
        sheet = wb[sheet_name]

        test_data = []
        for item in range(2,sheet.max_row+1):
            row_data = {}
            row_data['case_id'] = sheet.cell(item,1).value
            row_data['url'] = sheet.cell(item,2).value
            row_data['data'] = sheet.cell(item,3).value
            row_data['title'] = sheet.cell(item,4).value
            row_data['http_method'] = sheet.cell(item,5).value
            row_data['expected'] = sheet.cell(item,6).value
            test_data.append(row_data)

        return test_data

    @staticmethod
    def write_back(self,file_name,sheet_name,item,result,test_result):
        """写回结果数据"""
        wb = load_workbook(file_name)
        sheet = wb[sheet_name]
        sheet.cell(item,7).value = result
        sheet.cell(item,8).value = test_result
        wb.save(file_name)

if __name__ == '__main__':
    test_data = DoExcel().get_data("../test_data/test_data.xlsx",'login')
    print(test_data)
