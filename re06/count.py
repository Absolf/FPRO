#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 09:39:36 2018

@author: up201700135
"""

def count(word, phrase):
    word = word.lower()
    cont = 0
    
    for w in phrase.split():
        if w.upper() == word or w.lower()== word:
            cont +=1
    return cont

#
#w='Can'
#
#text='He can can a can better than a canner can can a can'
#
#result = count(w,text)
#
#print(result)