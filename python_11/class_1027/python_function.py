#!usr/bin/env python
#-*- coding:utf-8 -*-

#python内置函数
#特点：
#可以重复使用


#函数的语法：def 关键字
#函数名命名的规范：小写字母，不能以数字开头，不同的字母之间用下划线隔开
#def 函数名:
    #函数体（具体要实现的功能）

#调用：函数名()

def add_numbers():
    sum = 0
    for i in range(101):
        sum += i
    print("求和值是：{}".format(sum))
add_numbers()

#第一步：先用代码实现功能，还可以选取一组数据来证明是否正确
#第二步：变成函数，加def
#第三步：想办法提高代码的复用性

def add_numbers(m,n,k=1):
    sum = 0
    for i in range(m,n,k):
        sum += i
    print("求和值是：{}".format(sum))
add_numbers(1,101)