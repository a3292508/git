#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

# 类的语法
# class 类名：     #命名规范：1.数字字母下划线组成，不能以数字开头 2.首字母要大写 3.驼峰命名 4.如果参数为空，类名后可不加括号
#     类属性
#     类方法

class BoyFriend:
    #类属性
    height = 180
    weitht = 135
    money = '500w'
    name = 'zyj'

    #类方法/类函数
    def cooking(self):      #self:指这个实例本身,固定的占坑符号,类里面的方法，都必须带self这个参数
        print(self.name + '会做饭')

    def earn(self):
        print('会赚钱')

    def print_self(self):
        print(self)

    @classmethod
    def swimming(cls):
        print('会游泳')        #不可以调用类里面的属性值

    @staticmethod
    def sing():
        print('会唱歌')        #不可以调用类里面的属性值

#实例/对象 具体的一个例子  类名()
# bf = BoyFriend()        #实例具有类里面所有属性和方法的使用权限
# print(bf)               #实例存放的具体位置
# bf.print_self()         #调用类方法/类函数  实例.方法名()
# print(bf.height)        #调用属性  实例.属性名

#类里面方法是分为3种
#1.实例方法：意味着 这个方法 只能实例来调用
bf = BoyFriend()            #隐式的传递
BoyFriend.cooking(bf)       #显式的传递

#2.类方法:classmethod      可以不需要创建实例方法,实例和类名都可以直接调用
BoyFriend.swimming()
bf.swimming()

#3.静态方法:staticmethod    可以不需要创建实例方法,实例和类名都可以直接调用
BoyFriend.sing()
bf.sing()

#不同点：类方法和静态方法，不可以调用类里面的属性值，如果需要参数，需要自己传递

#什么时候去定义为类方法和静态方法？  当某个函数和其他的类函数/类属性，没有任何关系时，就可以定义为类方法和静态方法！！