#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-04 21:11
# @Author  : liukang
# @Site    : 
# @File    : test.py
# @Software: PyCharm


# LIST 是有序的，但是元组是无序的
res = [-1, 0, 0, 0, 0, 3, 3]
# set 之后还是一个无序的集合
# 这里是一个 小 bug
print(set(res))
# {0, 3, -1}
# {0, 3, -1}
