#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 21:47:29 2018

@author: laureano
"""

def flatten(alist):
    if alist == []:
        return alist
    if isinstance(alist[0], list):
        return flatten(alist[0]) + flatten(alist[1:])
    return alist[:1] + flatten(alist[1:])

#alist = ['Hello', [2, [[], False]], [True]]
#print(flatten(alist))