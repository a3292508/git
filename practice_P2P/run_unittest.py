#!usr/bin/env python
#-*- coding:utf-8 -*-

import unittest
from HTMLTestRunner import HTMLTestRunner
from practice_P2P.tools.test_http_request import TestHttpRequest
from practice_P2P.tools.project_path import *

suite = unittest.TestSuite()
# suite.addTest(TestHttpRequest('test_api'))
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(test_report_path,'wb') as file:
    runner = HTMLTestRunner(stream=file,
                            verbosity=2,
                            title='自动化测试',
                            description='test_api的单元测试报告')
    runner.run(suite)
