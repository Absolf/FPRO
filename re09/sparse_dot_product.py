#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 17:43:23 2018

@author: laureano
"""


def sparse_dot_vec(dict1, dict2):
    sum = 0
    for i in dict1:
        for j in dict2:
            if j == i:
                sum += dict1[i] * dict2[j]
    return sum


dict1 = {1: 3, 7: 1}
dict2 = {1: 3, 7: 1}

print(sparse_dot_vec(dict1,dict2))

























def sparse_dot_product(dict1, dict2):
    addition = 0
    for i in dict1:
        for j in dict2:
            if i == j:
                addition += dict1[i] * dict2[j]
#            else:
#                addition += 0
    return addition
            
    
    


dict1 = {1: 3, 7: 1}
dict2 = {1: 3, 7: 1}
print(sparse_dot_product(dict1, dict2))