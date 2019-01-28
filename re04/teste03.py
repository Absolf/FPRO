#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 20:21:28 2018

@author: laureano
"""

integers = [7, -3, 5, -1, 2, -4, 14, 0, -8, -14]
reals = [8.0, -4.6, 9.5 , -7.0, 11.0, -14.1, 13.4, -3.0, 10.0, -4.3]
result =""
new_integers = list(integers)

for i in range(len(integers)):
    if integers[i]>= reals[i]:
        result += str(integers[i])+" "
    else: 
        result += str(reals[i])+" "

print(result)
