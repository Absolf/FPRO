#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 11:42:06 2018

@author: laureano
"""

def triplet(atuple):
    size = len(atuple)
    found = True
    result =()
    for i in range(0, size-2):
        for j in range(i+1, size-1):
            for k in range(j+1, size):
                if (atuple[i] + atuple[j] + atuple[k]) == 0:
                    result += (atuple[i],atuple[j],atuple[k])                  
#    result = result[0:3]
    if(found==True):
        result = result[0:3]
    else:
        result = ()
    return result
atuple=(-1,1,1,1)

print(triplet(atuple))
                