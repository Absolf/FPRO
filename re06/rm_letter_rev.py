#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:28:34 2018

@author: up201700135
"""

def rm_letter_rev(l, astr):
    l = l.upper()
    for letter in astr:
        if letter.isalpha() and ((letter.upper() or letter.lower()) == l or letter == " "):
            astr = astr.replace(letter, "")
        else:
            astr = astr.replace(l, "")
        
    return astr[::-1]

#l=' '
#
#astr = 'a nut for a jar of tuna'
#
#result = rm_letter_rev(l,astr)
#
#print(result)