 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:09:55 2018

@author: laureano
"""
def palindrome(astring):
    cont = 0
    aux = len(astring)
    for i in range(aux):
        for j in range(i,aux):
            if j - i > 0:
                temp = astring[i:j+1]
                print(temp)
                if temp == temp[::-1]:
                    cont +=1
    result = ("For string '{}': {} palindrome substrings".format(astring,cont))
    return result
astring="banana"
print(palindrome(astring))

