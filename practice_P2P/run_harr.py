#!usr/bin/env python
#-*- coding:utf-8 -*-

from practice_P2P.tools.http_request import HttpRequest
from practice_P2P.tools.do_excel import DoExcel
from practice_P2P.tools.get_cookie import GetCookie

def run(test_data,sheet_name):
    for item in test_data:
        print("正在测试的用例是{0}".format(item['title']))
        res = HttpRequest().http_request(item['url'],eval(item['data']),item['http_method'],getattr(GetCookie,'Cookie'))
        if res.cookies:
            setattr(GetCookie,'Cookie',res.cookies)
        print("请求的结果是{0}".format(res))
        DoExcel().write_back("../test_data/test_data.xlsx",sheet_name,item['case_id']+1,str(res.json()))

test_data = DoExcel().get_data("../test_data/test_data.xlsx",'recharge')
run(test_data,'recharge')