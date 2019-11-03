#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

#文件的读写
#file文件open之后，默认是r，只读模式。如果要写入内容会报错！
#r+ 可读可写，先写的话，从头开始覆盖，读光标之后的内容，读写跟着光标走
#如果要写入中文的话，要注意编码格式，在后面加encoding='utf-8'（读和写尽量要分开，放一起的话也会报错）
#w 只写，要读的话会报错！      w+ 可读可写
#不管是w，还是w+，如果文件存在，就直接清空重写(慎重使用）；如果文件不存在，则新建一个文件，然后写
#不管是a，还是a+ 如果文件存在，就直接追加写，写在后面；如果文件不存在，则新建一个文件进行结果写入
#重点掌握r,a相关用法！

#r w a
#r+ w+ a+

#二进制
#rb rb+  wb wb+  ab ab+


# file = open('python11.txt','r',encoding='utf-8')
# res = file.read()
# print(res)

# file = open('python11.txt','r+',encoding='utf-8')
# res = file.read()       #进行一次读写之后，光标就到文末！光标默认是在开头！
# file.write('777')
# print(res)

# file = open('python22.txt','w',encoding='utf-8')    #文件不存在，则新建一个文件
# file.write('111')

#如何移动光标