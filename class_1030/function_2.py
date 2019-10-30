#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

#变量作用域
a = 1       #全局变量
def add(b):
    a =5    #局部变量
    print(a+b)

add(10)

#全局变量和局部变量
#1.作用范围不一样 全局变量：模块里都能用；函数的局部变量只能用于函数
#2.当全局变量和局部变量同名且同时存在时，函数优先调用局部变量
#3.当局部变量没有时，就优先用全局变量
#4.global
#5.一般情况下，谨慎使用全局变量，优先使用局部变量
def add(b):
    global a    #声明这是一个全局变量
    a = 5
    print(a + b)
add(10)
print(a)