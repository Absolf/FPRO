#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:23:45 2019

@author: laureano
"""

def compatible(A, B):
    try:
        if len(A[0]) != len(B):
            my_error = AssertionError('A and B cannot be multiplied')
            raise my_error
    except AssertionError as ex:
        return ex
    else:
        return 'A and B can be multiplied'
        
            
        
    
print(compatible([[2, 2, 3], [1, 1]], [[5, 5, 5, 5], [5, 5, 5, 5]]))
        