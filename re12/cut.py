#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 00:25:52 2018

@author: laureano
"""
def cut(filename, delimiter, field):
    aux = []
    result = []
    parts = ''
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            aux +=[lines[i]]
        for i in range(len(aux)):
            aux[i] = aux[i].split(delimiter)
            aux[i].insert(0,'0')
            for j in range(len(aux[i])):
                aux[i][j] = aux[i][j].replace('\n','')
        if isinstance(field,list):
            for i in range(len(aux)):
                for j in field:
                    parts += aux[i][j]+delimiter
                parts = parts[:-1]+'\n'
            result = parts
        else:
            for line in aux:
                result +=[line[field]]
            result = '\n'.join(result)
        return result


#print(cut("data.csv", ",", [2,4]))