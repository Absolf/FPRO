#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:08:01 2018

@author: laureano
"""
def isomorphic(astring1,astring2):
    dic_key_1 = dict()
    dic_key_2 = dict()
    is_isomorphic = True
    greater = []
    if len(astring1) == len(astring2):
        for i in range(len(astring1)):
            dic_key_1[astring1[i]] = astring2[i]
            dic_key_2[astring2[i]] = astring1[i]
    dic_val_1 = sorted(dic_key_1.values())
    dic_val_2 = sorted(dic_key_2.values())
    if len(dic_val_1) >= len(dic_val_2):
        greater = dic_val_1
        
    else:
        greater = dic_val_2 
        
    for j in range(len(greater)-1):
        if greater[j] == greater[j+1]:
            is_isomorphic = False
    items = list(dic_key_1.items())
    if is_isomorphic == True:
        return "'{}' and '{}' are isomorphic because we can map: %s".format(astring1,astring2) %items
    else:
        return "'{}' and '{}' are not isomorphic".format(astring1,astring2)
           
astring1 = 'turtle'
astring2 = 'tletur'

print(isomorphic(astring1,astring2))