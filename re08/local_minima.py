# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 18:58:16 2018

@author: laureano
"""
def local_minima(alist,n):
    n = n//2
    result = []
    new_list = []
    for idx,elem in enumerate(alist):
        if idx-n<0:
            new_list = alist[:idx+n+1]
            if elem == min(new_list):
                result += [(elem,idx)]
        else:
            new_list = alist[idx-n:idx+n+1]
            if elem == min(new_list):
                result += [(elem,idx)] 
    print(result)
    for j in range(1,n+1):
        for i in range(len(result)-j):
            if result[j][0] == result[i+1][0] and int(result[i][1])+j == int(result[i+1][1]):
                result.remove(result[i+1])
                break
    return result

alist = [10, 3, 3, 14, 5, 7, 4]
n = 3
print(local_minima(alist, n))