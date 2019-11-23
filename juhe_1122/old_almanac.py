#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

import unittest
from juhe_1122.http_request import HttpRequest

class OldAlmanac(unittest.TestCase):
    """测试用例"""
    def setUp(self):
        self.url='http://v.juhe.cn/laohuangli/d'
    def tearDown(self):
        pass
    def test_key_data_right(self):
        data = {"key":"aab6560e753c27e9a0ae2de368bb137d","date":"2019-11-22"}
        res = HttpRequest().http_request('post',self.url,data)
        try:
            self.assertEqual(0,res.json()['error_code'])
        except Exception as e:
            print('数据错误{}'.format(e))
            raise e

    def test_key_wrong(self):
        data = {"key":"aab6560e753c27e9a0ae2de368bb137d00","date":"2019-11-22"}
        res = HttpRequest().http_request('get',self.url,data)
        try:
            self.assertEqual(10000,res.json()['error_code'])
        except Exception as e:
            print('数据错误{}'.format(e))
            raise e

    def test_key_null(self):
        data = {"key":"","date":"2019-11-22"}
        res = HttpRequest().http_request('get',self.url,data)
        try:
            self.assertEqual(10001,res.json()['error_code'])
        except Exception as e:
            print('数据错误{}'.format(e))
            raise e

    def test_data_null(self):
        data = {"key":"aab6560e753c27e9a0ae2de368bb137d","date":""}
        res = HttpRequest().http_request('get',self.url,data)
        try:
            self.assertEqual(206501,res.json()['error_code'])
        except Exception as e:
            print('数据错误{}'.format(e))
            raise e

if __name__ == '__main__':
    unittest.main()