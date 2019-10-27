#!usr/bin/env python
#-*- coding:utf-8 -*-

#while循环语法：
# while 条件表达式：
#     代码块

#执行规律：首先判断while后面的条件表达式是否成立
#如果为True，那就执行代码块，执行完毕后继续判断--->还是True，那就执行代码块，执行完毕之后停止运行
#否则 不进入内部 执行代码块
#防止代码进入死循环：加一个变量来控制循环次数

"""
a = 1
while a<=5:
    print('现在是打印的第{0}次！'.format(a))
    a += 1

# 利用while循环，实现1-100的整数相加
a =0
sum = 0
while a <=100:
    sum += a
    a += 1
print(sum)
"""

i = 5
sum = 0
while i>=1:
    age = int(input('请输入年龄：'))
    sex = input('请输入性别：')
    if 10<=age<=12 and sex == 'woman':
        print('恭喜，符合条件哦')
        sum += 1
    else:
        print('不符合条件哦')
    i-= 1
print('符合条件的人数是{}'.format(sum))

#while 与 if 语句搭配使用continue,break？？？
