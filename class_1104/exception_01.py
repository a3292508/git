#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

#异常处理&调试

#异常：在代码运行过程中遇到的任何错误，带有error字样的，都是异常
#异常处理：我们对代码中所有可能会出现的异常，进行的处理

#1.处理某个错误   2.处理某种类型的错误     3.有错误就处理
#(1) try...except...
# import os
# try:
#     os.mkdir('python11')        #可能出错的代码
# except FileExistsError:         #出错的类型
#     print('已存在该文件！')      #进行处理
#
# try:
#     os.mkdir('python11')
# except OSError:                 #FileExistsError是OSError的一种更细分的错误类型，因此也可以处理成功
#     print('已存在该文件！')
#
# try:
#     os.mkdir('python11')
# except Exception:                         #只要出错，就会处理(Exception可加可不加）
#     print('已存在该文件！')
#
# try:
#     os.mkdir('python11')
# except NameError:                 #NameError和要处理的代码出错的类型不一致，因此不能成功处理
#     print('已存在该文件！')
#
# print('this is a test!')        #代码是从上到下执行的，如果前面的报错了，后面的不会执行

# import os
# try:
#     os.rmdir('python22')
# except Exception as e:      #把错误赋值给变量e,（e的意思是error，可以设置为其他变量，但一般用e）
#     print('未找到该文件！')
#     print('本次错误是{}'.format(e))
#     file = open('error.txt','a+',encoding='utf-8')
#     file.write(str(e)+'\n')
#
# print('测试成功！')

#(2)try...excpet...finally...
# import os
# try:
#     os.mkdir('python11')
# except NameError:
#     print('已存在该文件！')
# finally:        #不论是否出现异常，都要执行！
#     print('不管是否报错，依然执行！')

# (3)try...except...else...
import os
try:
    os.mkdir('python22')
except NameError:
    print('已存在该文件！')
else:        #try里的代码正常执行，这里才会执行！
    print('如果try里的代码不报错，这里就执行，否则不执行！')