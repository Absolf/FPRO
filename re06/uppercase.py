#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:00:13 2018

@author: up201700135
"""

def uppercase(astring):
    for w in astring[:3]:
        if w.isalpha() and w.upper() == w:
            return astring.upper()
    else:
        return astring
#
word ='Καλημέρα'
resultado = uppercase(word)
print(resultado)
#
