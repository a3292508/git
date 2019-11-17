#!usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from class_1117.unittest_01 import TestMathMethod
import HTMLTestRunner

#存储用例
suite = unittest.TestSuite()
#方法一：
#一个一个用例去执行，每次只执行一条
# suite.addTest(TestMathMethod('test_add_positive'))
# suite.addTest(TestMathMethod('test_sub_positive'))

#方法二：TestLoader
#创建一个加载器
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))     #从测试类中去寻找

#从模块里去找
# from class_1117 import unittest_01      #具体到模块
# suite.addTest(loader.loadTestsFromModule(unittest_01))


#执行
# file = open('test.txt','w+',encoding='UTF-8')
# #verbosity： 0:只返回错误用例的详细信息 1:返回成功和失败用例的个数 2：返回成功和失败用例的详细信息
# runner = unittest.TextTestRunner(stream=file,  verbosity=0)
# runner.run(suite)
# file.close()      #open之后需要关闭，否则会占用资源
# print(file.closed)      #判断文件是否关闭状态，返回True代表关闭，False代表未关闭

#上下文管理器
# with open('test.txt','w+',encoding='UTF-8') as file:
#     #verbosity： 0:只返回错误用例的详细信息 1:返回成功和失败用例的个数 2：返回成功和失败用例的详细信息
#     runner = unittest.TextTestRunner(stream=file,  verbosity=2)
#     runner.run(suite)

with open('report.html','wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title='单元测试报告',
                                           description='加法和减法测试')
    runner.run(suite)
