#!/usr/bin/python
#-*- coding:utf-8 -*-
#@Author：zhuxiujie

class GetData:
    Cookie = None   #存储cookie


if __name__ == '__main__':
    print(GetData.Cookie)
    setattr(GetData,'Cookie','session')
    print(hasattr(GetData,"Cookie"))
    print(getattr(GetData,"Cookie"))
    delattr(GetData,"Cookie")
    print(hasattr(GetData,"Cookie"))
#setattr()  可以直接把类里面的属性做修改
#hasattr()  判断是否有这个属性的值，有则返回True，否则False
#getattr()  获取属性的值
#delattr()  删除属性的值