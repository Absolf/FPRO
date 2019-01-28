# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:08:57 2018

@author: laure
"""


def capicua():
    result = "Not  yet implemented"
    reverse = 0
    temp = 0 
    n = int(input("Digite n: "))
    n_aux = n
    
        
    while n_aux > 0:
        temp = n_aux % 10
        n_aux = n_aux // 10
        reverse = reverse * 10 + temp
        
        
    if (n == reverse):
        result = str(n)+" is a palindrome"
    else:
        result = str(n)+" is not a palindrome"
    return result

print(capicua())
