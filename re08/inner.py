#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 09:36:04 2018

@author: laureano
"""
def inner(u,v):
    result = 0
    for i in range(len(u)):
        result +=u[i]*v[i]
    return result

u= [1, 2, 3, 4, 5]
v= [2, 3, 4, 5, 6]
print(inner(u,v))