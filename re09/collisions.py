#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 20:02:20 2018

@author: laureano
"""
def sum_digits(number):
    result = 0
    while number:
        result+= number % 10 
        number = number // 10
    return result
def collisions(alist):
    my_dict = dict()
    for element in alist:
        if element >= 10:
            temp = sum_digits(element)%8
            if temp not in my_dict:
                my_dict[temp] =1
            else:
                my_dict[temp] +=1
        else:
            temp = element%8
            if temp not in my_dict:
                my_dict[temp] = 1
            else:
                my_dict[temp] +=1
    return my_dict

alist = [24,42]
print(collisions(alist))
        
#for i in range(len(astring)):
#        if astring[i] in "aeiou".upper():
#            for j in range(len(astring[i:])):
#                if astring[i:j+1+i] in vowel_dict:
#                    vowel_dict[astring[i:j+1+i]] += 1  
#                else:   
#                    vowel_dict[astring[i:j+1+i]] =1
    