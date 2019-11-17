#!usr/bin/env python
#-*- coding:utf-8 -*-

#单元测试
import unittest
from class_1117.MathMethod import MathMethod

#1.用例执行顺序：按ASCII编码来执行！
#2.每个用例都是一个函数
#3.每个用例名称的第一个词必须是test，否则不会执行

class TestMathMethod(unittest.TestCase):
    """编写测试用例"""

    def setUp(self):
        print('开始执行测试！')

    def tearDown(self):
        print('测试结束！')

    def test_add_positive(self):
        """正数相加"""
        res = MathMethod(3,5).add()
        print('正数相加的结果是：',res)
        try:
            self.assertEqual(8,res)
        except AssertionError as e:
            print('断言错误是{0}'.format(e))
            raise e     #把异常处理完之后，要把它抛出去

    def test_add_nagitive(self):
        """负数相加"""
        res = MathMethod(-3,-9).add()
        print('负数相加的结果是：',res)
        try:
            self.assertNotEqual(-12,res,msg='-3+-9=-12')    #断言不通过时，会展示msg的内容
        except AssertionError as e:
            print('断言错误是{0}'.format(e))
            raise e

    def test_sub_positive(self):
        """正数相减"""
        res = MathMethod(8, 3).sub()
        print('正数相减的结果是：', res)
        try:
            self.assertEqual(5, res)
        except AssertionError as e:
            print('断言错误是{0}'.format(e))
            raise e

    def test_sub_nagitive(self):
        """负数相减"""
        res = MathMethod(-3,-9).sub()
        print('负数相减的结果是：',res)
        try:
            self.assertEqual(6, res)
        except AssertionError as e:
            print('断言错误是{0}'.format(e))
            raise e

if __name__ == '__main__':
    unittest.main()