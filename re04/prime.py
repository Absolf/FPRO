# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:42:58 2018

@author: laure
"""



def is_prime():
    result = "Not Implemented Yet"
    to_check = int(input("Digite o número: "))
    if to_check > 1:
        for i in range(2,to_check):
            if to_check % i == 0:
                result = False 
                break
        else:
            result = True
    else:
        result = False
    return result
    


print(is_prime())