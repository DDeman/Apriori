#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '任晓光'
__mtime__ = '2020/3/26'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""


def fun_2(data):
    res = []
    temp = []
    i = 0
    back_2(res, temp, i, data)
    return res


def back_2(res, temp, i, data):
    if i == len(data):
        return
    temp.append(data[i])
    tem = temp.copy()
    if len(tem) >= 2:
        res.append(frozenset(tem))
    back_2(res, temp, i + 1, data)
    temp.pop()
    back_2(res, temp, i + 1, data)