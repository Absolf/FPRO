#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 14:58:26 2018

@author: laureano
"""

def override(l1,l2):
   l22 = [item[0] for item in l2]
   l1=list(filter(lambda x: x[0] not in l22 , l1))
   return sorted(l1+l2)
                     
l1 = [('c','d'),('c','e'),('a','b'),('a', 'd')]
l2 = [('a','c'),('b','d')]

print(override(l1,l2))