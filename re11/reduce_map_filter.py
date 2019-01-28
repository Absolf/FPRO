#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 20:04:14 2018

@author: laureano
"""
from functools import reduce

def reduce_map_filter(args):
#    print(args[2][1])
    new_args = []
    if args[0] == 'map' and isinstance(args[2], tuple) == False:
        return list(map(args[1], args[2]))
    elif args[0] == 'filter' and isinstance(args[2], tuple) == False:
        return list(filter(args[1], args[2]))
    elif args[0] =='reduce' and isinstance(args[2], tuple) == False:
        return reduce((args[1]), args[2])
    else:
        if isinstance(args[2], tuple):
            if isinstance(args[2][2], tuple):
                result = reduce_map_filter(args[2][2])
            else:
                result = reduce_map_filter(args[2])
            new_args = tuple([str(args[2][0]),args[2][1], result])

           
        result = reduce_map_filter(new_args)
        new_args =  tuple([str(args[0]),args[1], result])       
        return reduce_map_filter(new_args)

args = ("map", lambda x: 2*x, [1,2,3])
#args =("map", lambda x: 2*x, ("filter", lambda x: x%2 != 0,[1,2,3]))
#args = ("reduce", lambda a,b: a+b,
#("map", lambda x: 2*x,
#("filter", lambda x: x%2 != 0,
#[1,2,3])))
print(reduce_map_filter(args))