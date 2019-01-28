#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:18:14 2018

@author: laureano
"""

def calculator(expr):
    if type(expr) == int:
        return expr
    else:
        op = expr[1]
        if op == '+':
            return calculator(expr[0]) + calculator(expr[2])
        elif op == '*':
            return calculator(expr[0]) * calculator(expr[2])
        elif op == '-':
            return calculator(expr[0]) - calculator(expr[2])

#expr = ((1, '+', 2), '*', 3)
#print(calculator(expr))
            