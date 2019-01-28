#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 21:25:08 2018

@author: laureano
"""
from functools import reduce as reduce

def map_reduce(n1, n2):
    if n1 % 2 == 0:
        n1 +=1
        if n1 == 1:
            n1 +=1
    sequence = list(x*x for x in range(n1,n2) if x%2 !=0)
    if len(sequence) < 50:
        return reduce(lambda x, y: x + y, sequence)
    else:
        return reduce(lambda x, y: x * y, sequence)
    
print(map_reduce(50,60))