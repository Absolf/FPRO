#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 19:52:10 2019

@author: laureano
"""

def raise_exception(alist, value):
    result = []
    for n in alist:
        try:
            if n <= value:
                my_error = ValueError("{0} is not greater than {1}".format(n,value),)
                raise my_error
        except ValueError as ex:
            result.append(ex)
    return result

print(raise_exception([1, -2, 3, 0], 3))