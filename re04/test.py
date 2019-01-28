#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 00:13:20 2018

@author: laureano
"""

def is_palindrome(word):
    result = False
    if word[::1] == word:
      result = True
    else:
      result = False
    return result
#word = input()
word = "adam"
print(is_palindrome(word))