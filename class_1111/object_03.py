#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

#类的继承

class RobotOne:

    def __init__(self,name,year):
        self.name = name
        self.year = year

    def walking(self):
        print(self.name + '只能行走，不能绕过障碍物！')

    def info(self):
        print(self.name + '的生产日期是{}'.format(self.year))

class RobotTwo(RobotOne):   #继承第一代机器人的类，父类有的都可以直接拿来用

    def jump(self):         #拓展：父类里没有的函数，都叫拓展
        print(self.name + '可以跳跃')

    def walking(self):     #子类里面的函数名与父类里面的函数名重复时，就叫重写!子类调用时，就会调用自己的！
        self.info()         #直接调用父类的函数
        print(self.name + '可以避开障碍物')

# t1 = RobotTwo('ET','2019')
# t1.walking()
# t1.info()


#多继承：继承多个父类
#父类之间不要有继承关系，否则会报错！！
#具有两个父类的属性和方法，如果两个父类具有同名方法时，就近原则，默认取第一个父类的

class RobotThree(RobotOne,RobotTwo):    #RobotOne,RobotTwo有继承关系，因此执行会报错，可以处理一下，使两者没有继承关系即可！

    def fly(self):
        print(self.name + '可以飞翔')

t3 = RobotThree('tony','2020')
t3.fly()