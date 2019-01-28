#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 14:45:23 2018

@author: laureano
"""
def aux_checker(matrix,word,row,letter):
    #base case
    if not word:
        return True
    elif word:
        for rows in range(row-1,row+2):
            for lines in range(letter-1,letter+2):
                if lines >= 0 and rows >= 0 and rows < len(matrix) and lines < len(matrix) and word[0] == matrix[rows][lines]:
                    matrix[rows][lines] == ''
                    if not aux_checker(matrix,word[1:],rows,lines):
                        continue
                    else:
                        return aux_checker(matrix,word[1:],rows,lines)

def soup(matrix,word):
    for row in range(len(matrix)):
        for letter in range(len(matrix[row])):
            if matrix[row-1][letter-1] == word[0]:
                #call to the recursive function
                if aux_checker(matrix,word[1:],row-1,letter-1):
                    return f"{chr(ord('A')+row-1)}{letter}"
                
#mx = (('X', 'A', 'B', 'N', 'T', 'O'),
#      ('Y', 'T', 'N', 'R', 'I', 'T'),
#      ('U', 'P', 'O', 'M', 'D', 'S'),
#      ('I', 'O', 'H', 'U', 'O', 'O'),
#      ('R', 'T', 'E', 'L', 'Q', 'X'),
#      ('I', 'W', 'J', 'K', 'P', 'Z'))
#
#print(soup(mx, 'HELLO'))