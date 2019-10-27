#!usr/bin/env python
#-*- coding:utf-8 -*-

#列表
#1.可以存在空列表[]
#2.列表里面可以包含任何类型的数据
#3.列表里面的元素，用逗号来进行分隔
#4.列表里的元素也有索引，从0开始
#5.获取列表里面的单个值：列表[索引值]
#6.列表的切片，同字符串的操作一致，即列表名[索引头:索引尾:步长]

#列表可以存储数据
#如果要存储的数据是同一个类型的，建议用列表
list_01 = [1,2.00,'list',[1,2,3],True]
print(len(list_01))
print(list_01[3])
print(list_01[1:4:2])

#增加数据:append()方法，一次只能插入一个值
list_01.append('john')
print('list_01的值是{}'.format(list_01))
#插入数据：insert()方法,要指定索引值
list_01.insert(4,10)
print('list_01的值是{}'.format(list_01))
#删除数据：pop()方法，不指定索引值则默认删除最后一个值
list_01.pop()
res = list_01.pop(2)
print(res)      #返回被删除的元素
print('list_01的值是{}'.format(list_01))
#修改列表：
list_01[2] = 'soul'
print('list_01的值是{}'.format(list_01))
