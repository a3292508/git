#!usr/bin/env python
#-*- coding:utf-8 -*-

# 绝对路径
# C:\Users\17486\PycharmProjects\python_11\class_1103\path_01.py
#相对路径

import os
#新建一个目录/新建一个文件夹
# os.mkdir('file_os')

#跨级新建目录：用/符号来代表路径的不同等级
#必须确保上面的层级是存在的
# os.mkdir('file_os/os_01')
# os.mkdir('C:\ltest_python')
# os.mkdir(r'C:\test_python')     #可以通过加r/R，或\来让转义字符失效

#转义字符
# 换行：\n
# 横向制表符：\t
# 回车：\r

#删除文件夹  也是一级一级的删除
# os.rmdir('file_os/os_01')
# os.rmdir('file_os')     #报错：OSError: [WinError 145] 目录不是空的。

# 拓展：python可否强制删除？？？
#如何新建文件/删除文件？？？

#路径的获取1     获取当前工作目录，具体到最后一级目录
# path = os.getcwd()
# print('当前路径为：{}'.format(path))

#路径的获取2     获取当前文件所在的绝对路径，具体到模块名
# path2 = os.path.realpath(__file__)      #__file__指的是当前文件本身
# print('当前路径为：{}'.format(path2))

#路径的获取3     获取当前文件所在的绝对路径，具体到模块名
# path3 = os.path.abspath(__file__)
# print('当前路径为：{}'.format(path3))

#如何拼接路径
# new_path = os.getcwd() + '\python_11'
# new_path = os.getcwd() + '/python_11'     python中，正斜杠和反斜杠/双斜杠没有任何区别
# new_path = os.getcwd() + '//python_11'
# print(new_path)
# os.mkdir(new_path)

#join方法
# new_path2 = os.path.join(os.getcwd(),'python666')
# print(new_path2)
# os.mkdir(new_path2)

#判断是否是文件（文件返回True）
print(os.path.isfile(__file__))
print(os.path.isfile(os.getcwd()))

#判断是否是目录（目录返回True）
print(os.path.isdir(__file__))
print(os.path.isdir(os.getcwd()))

#判断文件是否存在
os.path.exists(r'C:\Users\17486\PycharmProjects\python_11\class_1101\do_file.py')

#罗列当前路径的所有文件和目录
print(os.listdir(os.getcwd()))

#拓展题
#给定一个路径，打印出所有的路径（直到这个路径下没有目录为止）
#思路：递归函数（写成一个函数）
for path in os.listdir(os.getcwd()):
    if os.path.isdir(path):
        os.listdir(os.path.join(os.getcwd(),path))
        print('{0}还需要进一步处理'.format(path))
    else:
        print('这个是已经穷尽的路径',os.path.join(os.getcwd(),path))