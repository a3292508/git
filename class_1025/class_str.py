#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

s = 'hello,python!'
#切片：字符串名[索引头:索引尾:步长]，步长默认为1
#正序
print(s[4])
#取头不取尾
print(s[1:4])
#步长设置为2
print(s[1:5:2])
#默认从头开始，取头不取尾
print(s[:4])
#默认从第5开始，一直取到最后值
print(s[4:])
#反序：最后一个值
print(s[-1])
#索引头和尾都默认为空，反序输出所有的值
print(s[::-1])
#反序输出所有的值，步长需要为负数（默认-1）
print(s[-1:-14:-1])

#字符串的分割：split()方法（可以指定切割符号，切割次数）
#分割后，返回一个列表类型的数据，列表里面的子元素都是字符串类型
print(s.split())
#指定的切割符被切走了
print(s.split(','))
#切割2次（若被切割的字符在一起，会返回一个空字符串）
print(s.split('l',2))

#字符串的替换：replace()方法（指定替换值，新值，替换次数）
#默认替换所有的指定替换值
print(s.replace('o','@'))
#替换次数设置为1次,只替换前面的1个
print(s.replace('o','@',1))

#字符串的去除：strip()方法（去除字符串首尾所有指定的字符）
s = ' !hel!lo!'
#去除字符串前后的空字符串
print(s.strip())
s = '!hel!lo!'
#去除字符串首尾所有指定的字符
print(s.strip('!'))

#字符串的拼接（+号）:+号左右两边的变量值类型要一致
s_1 = 'python'
s_2 = '国庆节'
print(s_1+s_2)

#字符串的格式化输入
# 1.format :特点是{}占坑，默认是按顺序填坑
age = 18
name = 'john'
score = 99.99
print('{}的年龄是{}'.format(name,age))
print('{1}的年龄是{0}'.format(age,name))
# 2.%  %s字符串  %d数字  %f浮点数
#%s 可以填任何数据
#%d 只能填数字 整型 浮点数
#%f 只能填数字,默认展示6位小数，可以通过<%.数字f>指定长度,只指定1位时还会四舍五入
print('%s的年龄是%d,考了%f'%(name,age,score))
print('%s的年龄是%d,考了%.1f'%(name,age,score))
print('%s的年龄是%d,考了%.2f'%(name,age,score))
#%s 可以填任何数据
print('%s的年龄是%d,考了%s'%(name,age,score))