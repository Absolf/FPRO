#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:00:45 2018

@author: laureano
"""

def find_dtype(atuple, data_type):
#    empty = ()
    lista = []
    for element in atuple:
        if type(element).__name__ == data_type:
            lista.append(element)
    return tuple(lista)
    

    
    
atuple = (1, False, "hello", 2., "world")
data_type="str"

print(find_dtype(atuple, data_type))

print(type("world"))
