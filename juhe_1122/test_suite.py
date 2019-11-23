#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

import unittest
from juhe_1122.old_almanac import OldAlmanac
from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
loader = unittest.TestLoader()

# suite.addTest(loader.loadTestsFromModule(OldAlmanac))
suite.addTest(loader.discover('./', pattern='test*.py'))

with open('old_report.html','wb') as file:
    runner = HTMLTestRunner(stream=file,
                            verbosity=1,
                            title="自动化测试报告",
                            description="用例执行结果")
    runner.run(suite)
