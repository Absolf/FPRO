# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:55:22 2018

@author: laure
"""
def fizzBuzz():
    answer =" "
    n = int(input("Digite o limite do jogo: "))
    for fizzbuzz in range(1, n+1):
       
        if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
            continue
        elif fizzbuzz % 3 == 0:
            answer+=' Fizz'
        elif fizzbuzz % 5 == 0:
            answer+=' Buzz'  
        else:
            answer+= " " + str(fizzbuzz)
    return answer
    


print(fizzBuzz())
    


    

    
    