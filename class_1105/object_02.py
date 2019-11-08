#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

#初始化函数:__init__(self)
#__int__()不是初始化函数，不要搞错！


class BoyFriend:
    def __init__(self,name,age):     #接收的是外部值
        self.name = name            #把外部的值赋值给类属性
        self.age = age


    def cooking(self):
        print(self.name + '会做饭')

    def earn(self):
        print(self.name + '会赚钱')

    def age_01(self):
        print(self.name + '的年龄是' + self.age)

bf = BoyFriend('小何','22')
bf.age_01()

#什么时候需要用初始化函数？
#想用就可以用
#如果某个属性值是多个函数共用的，就可以用初始化函数（提高复用性）