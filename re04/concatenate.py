# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:54:18 2018

@author: laure
"""


    
        
def concatenate():  
    result = "Not yet implemented"
    num1 = int(input ('n1: '))
    num2 = int(input ('n2: '))
    num_2_aux = num2
    
    conc = 0
    cont = 0
    if num2 != 0:
        while num_2_aux > 0:
            num_2_aux = num_2_aux // 10
            cont +=1
        power = cont
        conc = num1 * (10** power) + num2
        result = conc
    else:
        result = num1
    return result

print(concatenate())  

            
    
    
        