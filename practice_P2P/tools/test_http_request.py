#!usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from practice_P2P.tools.http_request import HttpRequest
from practice_P2P.tools.get_data import GetData
from ddt import ddt,data
from practice_P2P.tools.do_excel import DoExcel
from practice_P2P.tools.project_path import *
from practice_P2P.tools.my_log import MyLog

test_data = DoExcel().get_data(test_data_path)       #执行的用例

@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*test_data)
    def test_api(self,item):
        res = HttpRequest().http_request(item['url'],eval(item['data']),item['http_method'],getattr(GetData,'Cookie'))
        if res.cookies:     #利用反射，存储cookies值
            setattr(GetData,'Cookie',res.cookies)
        try:
            self.assertEqual(str(item['expected']), res.json()['code'])
            test_result = 'PASS'
        except Exception as e:
            test_result = 'Failed'
            # print("执行用例出错：{0}".format(e))
            MyLog().info("执行用例出错：{0}".format(e))
            raise e
        finally:
            # print("获取到的结果是：{0}".format(res.json()))
            MyLog().info("获取到的结果是：{0}".format(res.json()))
            DoExcel.write_back(test_data_path,item['sheet_name'],item['case_id']+1,str(res.json()),test_result)

if __name__ == '__main__':
    unittest.main()