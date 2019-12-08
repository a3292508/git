#!usr/bin/env python
#-*- coding:utf-8 -*-

from practice_P2P.tools.http_request import HttpRequest
from practice_P2P.tools.do_excel import DoExcel
COOKIE = None

def run(test_data,sheet_name):
    global COOKIE
    for item in test_data:
        print("正在测试的用例是{0}".format(item['title']))
        res = HttpRequest().http_request(item['url'],eval(item['data']),item['http_method'],COOKIE)
        if res.cookies:
            COOKIE = res.cookies
        print("请求的结果是{0}".format(res))
        DoExcel().write_back("../test_data/test_data.xlsx",sheet_name,item['case_id']+1,str(res.json()))

test_data = DoExcel().get_data("../test_data/test_data.xlsx",'register')
run(test_data,'register')

test_data = DoExcel().get_data("../test_data/test_data.xlsx",'login')
run(test_data,'login')

test_data = DoExcel().get_data("../test_data/test_data.xlsx",'recharge')
run(test_data,'recharge')


#如果不用case_id来写入结果，可以使用这种方法！
# def run(test_data):
#     for i in range(len(test_data)):
#         print("正在测试的用例是{0}".format(test_data[i]['title']))
#         res = HttpRequest().http_request(test_data[i]['url'],eval(test_data[i]['data']),test_data[i]['http_method'])
#         print("请求的结果是{0}".format(res))
#         DoExcel().write_back("../test_data/test_data.xlsx",'login',i+2,str(res.json()))