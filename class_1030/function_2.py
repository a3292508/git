#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

#变量作用域
# a = 1       #全局变量
# def add(b):
#     a =5    #局部变量
#     print(a+b)
#
# add(10)

#全局变量和局部变量
#1.作用范围不一样 全局变量：模块里都能用；函数的局部变量只能用于函数
#2.当全局变量和局部变量同名且同时存在时，函数优先调用局部变量
#3.当局部变量没有时，就优先用全局变量
#4.global
#5.一般情况下，谨慎使用全局变量，优先使用局部变量

# def add(b):
#     global a    #声明这是一个全局变量
#     a = 5
#     print(a + b)
# add(10)
# print(a)

#怎么引入不同的模块--->
#第三方库
#a.在线安装  1)打开cmd--->pip install 模块名
#2)使用国内源去进行安装 pip install 国内源地址 模块名
#3）file--setting--project interpreter-->+
#b.离线安装
#1)在网上找到离线安装包;2)解压;3)拷贝解压后的文件到python安装路径;4)到cmd中进入到安装包文件路径，安装文件 python setup.py install

#怎么用
#1.python自带的/或第三方库：1)import...     2)from ...import...(至少精确到模块名，到包名不可以）
#import email.mime.base
#from email.mime import base
#2.自己写的

# if __name__ == '__main__':  #主程序的执行入口，只有在当前模块下执行时，才会执行下面的所有代码；其他文件引入时，只执行引入的代码
#     print('1')
#     print('hero')

