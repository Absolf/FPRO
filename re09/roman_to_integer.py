#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:05:28 2018

@author: laureano
"""

def roman_to_integer(astring):
    total = 0
    astring = astring.upper()
    romans = {'I': 1,'V': 5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    for i in range(len(astring)-1):
        if romans[astring[i+1]] <= romans[astring[i]]:
            total += romans[astring[i]]
        else:
            total -= romans[astring[i]]
    total += romans[astring[-1]]
    return total

astring = 'MMMCMXCIX'

print(roman_to_integer(astring))