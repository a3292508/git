#!usr/bin/env python
#-*- coding:utf-8 -*-
import yaml
fs = open('demo.yaml')
datas = yaml.load(fs)
print(datas)
