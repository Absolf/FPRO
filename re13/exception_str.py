#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 18:56:12 2019

@author: laureano
"""

def exception_str(f):
    try:
        f()
    except Exception as e:
        s = str(e)
        return s
    else:
        return 'No exception was raised'
        
print(exception_str(lambda: 0))