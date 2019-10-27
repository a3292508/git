#!usr/bin/env python
#-*- coding:utf-8 -*-

# if判断语句：分支分流
# if    elif    else
#if后面的语句满足条件时，才会执行子语句!

#空数据==False  非空数据==True
#布尔值False也代表否定，True代表确定
g = ''
h = []
i = {}
j = ()
if g:
    print('打印成功')   #不打印

if False:
    print('打印成功')   #不打印

#1.if...else...
age = 22
if age>20:
    print("恭喜你可以领结婚证了！")
else:
    print('革命尚未成功，同志仍须努力')

#2.if...elif...else...
age = 18
if age>=20:
    print("恭喜你可以领结婚证了！")
elif 8<=age<20:
    print('革命尚未成功，同志仍须努力')
else:
    print('你还是个baby')


#input函数：从控制台获取一个数据，获取的数据类型都是字符串类型！
#int()方法：将字符串转换为整数
#str()方法：将其他元素转换为字符串
#isdigtal()方法：判断输入的数据是不是只由数字组成
"""
age = int(input('请输入你的年龄：'))
if age>20:
    print("恭喜你可以领结婚证了！")
else:
    print('革命尚未成功，同志仍须努力')
"""
"""
score = input('请输入你的成绩：')
if score.isdigit():
    if int(score)>=90:
        print('优秀')
    elif 60<int(score)<90:
        print('良好')
    else:
        print('不及格')
else:
    print('请输入数字！')
"""

#随机数生成
import random
#随机生成0~9任一整数
number_01 = random.randint(0,9)
print(number_01)
#随机生成1~2中间的实数
number_02 = random.uniform(1,2)
print(number_02)
#可以设置步长，从9，19，，，99随机生成一个实数
number_03 = random.randrange(9,100,10)
print(number_03)