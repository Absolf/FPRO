# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 00:02:48 2018

@author: laure
"""

def is_perfect(n):
    #n = int(input("n: "))
    soma = 0
    result = True
    for i in range(1,n):
        if n % i == 0:
            soma +=i
    if soma == n:
        result = True
    else:
        result = False
    return result



result = is_perfect(num)

print(result)
        