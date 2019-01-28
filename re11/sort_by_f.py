#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 23:14:51 2018

@author: laureano
"""


def sort_by_f(l):
    return sorted(l, key = lambda x: 5 - x if x>=5 else x)

l = [-1, -2, 2, 15, 99]
print(sort_by_f(l))
