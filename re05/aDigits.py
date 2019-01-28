# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 01:27:52 2018

@author: laure
"""
import math

def adigits(n1,n2,n3):
    
    s1 = int(n1)
    s2 = int(n2)
    s3 = int(n3)
    numbers = [s1,s2,s3]
    
    n_max = max(numbers)
    #print(n_max) find the maximum number in the list
    if s1 == s2 or s1 == s3:
        median = s1
    if s2 == s3 or s2 == s1:
        median = s2
    if s3 == s1 or s3 == s2:
        median = s3
    else:
        median = math.ceil(sum(numbers)/len(numbers))
    #print(median) find the midle number in the list
    n_min = min(numbers)
    #print(n_min) find the lower number in the list
    
    result = int(str(n_max) + str(median) + str(n_min))
    return result

print(result)