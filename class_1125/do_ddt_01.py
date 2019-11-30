#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

#ddt
from ddt import ddt,data,unpack
import unittest

# test_data = [[1,3,5],[8,9]]
#
# @ddt    #装饰测试类
# class TestMath(unittest.TestCase):
#
#     @data(*test_data)   #装饰测试方法，拿到几个数据，就执行几条用例
#     @unpack             #根据逗号拆分拿到的参数，接受到几个就必须设置几个变量，必须对等(可设置默认值None）
#     def test_print_data(self,a=None,b=None,c=None):
#         print("a:",a)
#         print("b:",b)
#         print("c:",c)

#如果unpack后的参数，少于5个，推荐使用unpack
#要注意参数不对等的情况，提供相应个数的参数来接收变量

#脱外套：前面加个*号，会每拿到一条数据就执行一次
#list_01 = [1,2,3]
#print(*list_01)

test_data_2 = [{"no":1,"name":"john"},{"no":2,"name":"mac"}]
@ddt
class TestMath_1(unittest.TestCase):

    @data(*test_data_2)
    @unpack         #如果要对字典进行unpack，参数名要对应字典里的key名
    def test_print_data(self,no,name):
        print("no:",no)
        print("name:",name)
