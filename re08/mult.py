#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:24:30 2018

@author: laureano
"""
def mult(M, N):
    r = []
    if (len(M[0]) != len(N)) or (len(M[0]) == 0):
        result = []
    else:
        for l in M:
            r.append([])
        for i, c in enumerate(M):
#            print(c)
            for j in range(len(N[0])):
#                print(N[j])
                cont = 0
                for k in range(len(N)):
                    cont += c[k]*N[k][j]
                r[i].append(cont)
        result = r                   
    return result

M = [[1, 2, 3], [4, 5, 6]]
N = [[9], [8], [7]]

print(mult(M,N))
