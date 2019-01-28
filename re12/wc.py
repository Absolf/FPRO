#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 00:00:16 2018

@author: laureano
"""

def wc(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        words =''
        for w in lines:
            if w == ' ' or w =='':
                continue
            else:
                words += w

        return (len(lines),len(words.split()),len(words))
    
#print(wc('shakespeare.txt'))
        
        
    