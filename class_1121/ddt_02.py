#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

# eval()方法：把数据类 转换成 原本的数据类型
#仅限于字符串和其他类型的转换，如布尔值、数字、字典、列表、元祖等
s = 'True'
print(s,type(s))
print(eval(s),type(eval(s)))

t = '{"age":18}'
print(t,type(t))
print(eval(t),type(eval(t)))