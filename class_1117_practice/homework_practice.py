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
# COOKIE = None
from class_1117_practice.get_data import GetData

class TestHttp(unittest.TestCase):
    """测试用例"""

    def setUp(self):
        self.login_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
        self.recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'

    def tearDown(self):
        pass

    def test_login_success(self):
        # global COOKIE       #声明全局变量
        data = {"username":"16602159899","password":"123456"}
        res = HttpRequest().http_request('post',self.login_url,data)
        if res.cookies:     #如果cookie有的话，就更新COOKIE
            # COOKIE = res.cookies
            setattr(GetData,'Cookie',res.cookies)       #反射
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

    def test_recharge_success(self):
        # global COOKIE
        data = {'mobilephone':'18003831018','amount':'1000'}
        # res = HttpRequest().http_request('post', self.recharge_url, data,COOKIE)
        res = HttpRequest().http_request('post', self.recharge_url, data, getattr(GetData,'Cookie'))
        try:
            self.assertEqual('10001',res.json()['code'])
        except AssertionError as e:
            print('error is {}'.format(e))
            raise e

    def test_recharge_failure(self):
        # global COOKIE
        data = {'mobilephone':'18003831018','amount':'-300'}
        # res = HttpRequest().http_request('post', self.recharge_url, data,COOKIE)
        res = HttpRequest().http_request('post', self.recharge_url, data, getattr(GetData, 'Cookie'))
        try:
            self.assertEqual('20117',res.json()['code'])
        except AssertionError as e:
            print('error is {}'.format(e))
            raise e

if __name__ == '__main__':
    unittest.main()

#如何解决cookie问题，或数据之间相互依赖的问题（第二个接口要用到第一个接口的返回值）？
#1.全局变量global
# 缺点：关联性比较强，一步错步步错
#2.反射：
#setattr()  可以直接把类里面的属性做修改
#hasattr()  判断是否有这个属性的值，有则返回True，否则False
#getattr()  获取属性的值
#delattr()  删除属性的值
# 缺点：关联性比较强，一步错步步错

#3.写进setUp()中
