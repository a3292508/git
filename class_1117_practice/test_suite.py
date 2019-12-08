#!usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from HTMLTestRunner import HTMLTestRunner
# from class_1117_practice.homework_practice import TestHttp
from class_1117_practice import homework_practice

suite = unittest.TestSuite()

loader = unittest.TestLoader()

suite.addTest(loader.loadTestsFromModule(homework_practice))

with open('test_report.html','wb') as file:
    runner = HTMLTestRunner(stream=file,
                            verbosity=1,
                            title='自动化测试报告',
                            description='测试用例执行结果')
    runner.run(suite)