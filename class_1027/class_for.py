#!usr/bin/env python
#-*- coding:utf-8 -*-

#for循环语法：
#for item in 某个数据类型（字符串/列表/元祖/字典/集合等）：
    #代码块
#遍历元素，然后赋值给item
#循环次数，由数据的元素个数决定

"""
数据类型是字典的话，只打印key
dict_01 = {'age':22,'sex':'woman'}
for i in dict_01:
    print(i)
    print(dict_01[i])
"""
"""
L = [5,6,9,3,7]
sum = 0
for i in L:
    sum += i
print(sum)
"""

#range()函数：
#range(m,n,k) m是头，默认为0；n是尾；k是步长，默认为1，取头不取尾
"""
sum = 0
for item in range(5):
    age = int(input('你的年龄是：'))
    sex = input('你的性别是：')
    if 10<=age<=12 and sex == 'woman':
        print('你被录取了')
        sum += 1
    else:
        print('对不起，不符合条件')
print('符合条件的人数是：{0}'.format(sum))

#根据L的索引值，打印列表中每个元素的值
L = [5,6,9,3,7]
for i in range(len(L)):
    print(L[i])

#算出1-100整数相加的和（包含1，100）
sum = 0
for i in range(1,101):
    sum += i
print(sum)

#嵌套循环
#打印列表中的每一个元素
L = [['1','2','3'],[4,5,6,7]]
for i in L:
    for a in i:
        print(a)
"""

#利用for循环生成一个直角三角形
for i in range(1,5):
    print(i * '*')
print('-------')
#利用for循环生成一个倒直角三角形
for i in range(5,0,-1):
    print(i*'*')
