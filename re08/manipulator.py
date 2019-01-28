#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 23 14:36:16 2018

@author: laureano
"""
def manipulator(l, cmds):
    result=""
    for idx in cmds:
        idx=idx.split()
        if idx[0]=="insert":
            l.insert(int(idx[1]),int(idx[2]))
        elif idx[0]=="append":
            l.append(int(idx[1]))
        elif idx[0]=="print":
            result+= str(l) + " "
        elif idx[0]=="remove":
            l.remove(int(idx[1]))
        elif idx[0]=="pop":
            l.pop()
        elif idx[0]=="sort":
            l.sort()
        elif idx[0]=="reverse":
            l.reverse()
    return result

l = [2, 4]
cmds =  ["print", "remove 4", "append 1", "sort","print", "pop", "reverse", "print"]  
print(manipulator(l,cmds))
