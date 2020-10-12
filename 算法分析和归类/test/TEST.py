#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-12 15:09
# @Author  : liukang
# @Site    : 
# @File    : TEST.py
# @Software: PyCharm

import arrow

data = None
print(len(data))
tz_postfix = "+07:00"
now = arrow.now(tz=tz_postfix).strftime("%Y-%m-%d")
print(now)
