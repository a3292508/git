#!usr/bin/env python
#-*- coding:utf-8 -*-

#超继承
# super（子类的名称，self）

class MathMethod:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

    def sub(self):
        return self.a + self.b


class MathMethod_01(MathMethod):
    def divide(self):
        return self.a - self.b

    def add(self):
        super(MathMethod_01,self).add()     #超继承：super（子类的名称，self）
        print(self.a +self.b + 10)

MathMethod_01(12,20).add()
