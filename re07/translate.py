#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 15:23:08 2018

@author: laureano
"""


def translate(astring, table):
    astring = list(astring)
    for tup in table:
        for letter in astring:
            if tup[0] == letter:
                astring[astring.index(letter)]= str(tup[1]) 
    
    return ''.join(astring)

astring="unintelligible words...!"
table=(('l', 'k'), ('e', 'l'), ('i', 'u'), ('.', '??'))
    
print(translate(astring, table))


            
    