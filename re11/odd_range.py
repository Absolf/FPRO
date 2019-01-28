#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:31:17 2018

@author: laureano
"""
def odd_range(start, stop, step):
    if (start%2) == 0:
        start += 1
    sequence = list(range(start,stop,step*2))
    for item in sequence:
        if item % 2 != 0:
            yield item

print(list(odd_range(1, 10, 1)))
#print(list(odd_range(100,150,5)))
        