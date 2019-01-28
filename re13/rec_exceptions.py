#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:03:13 2019

@author: laureano
"""

def rec_exceptions(l):
    result = []
    for func in l:
        try:
            func()
        except Exception as ex:
            result += [ex]
        else:
            result += rec_exceptions(func())
    return result

print(rec_exceptions([lambda: [lambda: [1,2,3].index(-1), lambda:
''[2]], lambda: [1,2,3][4], lambda: [lambda: [lambda: 1/0]]]))
