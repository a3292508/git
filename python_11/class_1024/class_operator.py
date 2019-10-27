#!usr/bin/env python
#-*- coding:utf-8 -*-

#运算符 5大类：+ - * / %
#模运算/取余运算：用于判断某个数是偶数还是奇数
a = 5
print(a%2)

#赋值运算符：= += -=
b = 6
b += 1  #等同于b=b+1
print(b)
b -= 2  #等同于b=b-2
print(b)

#比较运算符 > >= < <= != == 6种比较关系
# 比较结果返回的值是布尔值，True,False
c = 7
d = 8
print(c>d)
print(c<d)
print(c!=d)
print(c==d)

#python区分大小写
#upper()方法：字符串的字母全都变成大写
#lower()方法：字符串的字母全都变成小写
print('get'=="GET")     #结果是False
print('get'.upper()=="GET")
print('get'=="GET".lower())

#逻辑运算符 and or not
#逻辑运算结果返回的值是布尔值，True,False
#and 左右两边结果都为真才是真，只有一个为假就都为假
#or 左右两边结果都为假才是假，只要有一个为真就是真

#成员运算符 in not in
#返回值也是布尔值 True,False
e = {'age':18,'name':'vae'}
print('age' in e)
print(18 in e)      #结果为False，因为字典是判断key值！