# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def unique(atuple):#my initial idea
    l_tuple = atuple
    l_tuple = set(l_tuple)
    l_tuple = tuple(sorted(l_tuple))
    return l_tuple

def unique2(atuple):#miguel's help
    return tuple(sorted(set(atuple)))
    
atuple = (8, 8, 1, 3, 1, 3, 5)

print(unique(atuple))
print(unique2(atuple))