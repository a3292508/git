#!usr/bin/env python
#-*- coding:utf-8 -*-

#1.提供2个接口：
#登录url='http://119.23.241.154:8080/futureloan/mvc/api/member/login'
# 接口返回值：{'data':None,'code':'10001','status':1,'msg':'登录成功'}
#充值url='http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
#2.针对登录接口写4个用例：正常登录/不输入密码/不输入账号/输入错误的密码
#3.充值接口写4个用例：正常充值/不输入账号/不输入金额/输入错误的金额-负数
#4.利用任何一种方法实现用例的加载并执行
#5.生成html类型的测试报告
#6.在测试类里面加上异常处理及断言

import unittest
from class_1117_practice.object_pack import HttpRequest

class TestHttp(unittest.TestCase):
    """测试用例"""

    def setUp(self):
        self.login_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
        self.recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'

    def tearDown(self):
        pass

    def test_login_success(self):
        data = {"username":"16602159899","password":"123456"}
        res = HttpRequest().http_request('post',self.login_url,data)
        try:
            self.assertEqual('10001',res.json()['code'])
        except AssertionError as e:
            print('error is {}'.format(e))
            raise e

    def test_login_wrongpwd(self):
        data = {"username":"16602159899","password":"12345678"}
        res = HttpRequest().http_request('post',self.login_url,data)
        try:
            self.assertEqual('20111',res.json()['code'])
        except AssertionError as e:
            print('error is {}'.format(e))
            raise e
    #
    # def test_recharge_success(self):
    #     data = {'mobilephone':'18003831018','money':'1000'}

if __name__ == '__main__':
    unittest.main()