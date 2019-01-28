#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 00:04:54 2018

@author: laureano
"""

def parse(filename):
    with open(filename, "r") as f:
        aux =  [i.strip("\n ") for i in f.readlines()]
        result = ''
        for i in aux:
            if i == "(":
                result += "("
            else:
                result += i + ","
        result = "("+result+")"
        return eval(result)

print(parse('tuple1.txt'))