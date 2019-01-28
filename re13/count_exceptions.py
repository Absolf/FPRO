#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:07:47 2019

@author: laureano
"""

def count_exceptions(f, n1,n2):
    cont = 0
    for n in range(n1,n2+1):
        try:
            f(n)
        except Exception:
            cont +=1
    return cont

#print(count_exceptions(lambda x: 1/0 if x > 10 else 0, 0, 50))
                
            
        