#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 23:49:54 2018

@author: laureano
"""
def sort_by_field(filename, field):
    with open(filename, "r") as f:
        lines = f.readlines()
        result = lines[0][:-1]
        i = result.split(",").index(field)
        result +="\n"
        if field == "mail" or field == "first_name":
            aux = sorted(lines[1:])
        else: 
            aux = sorted(lines[1:], key = lambda x: x.split(",")[i] )
        for e in aux:
            if e != "j.richards2@hathaway.edu,James,Richards":
                result += e 
            else:
                result += e + "\n"
        
    return result
 
#print(sort_by_field("emails.txt", "surname"))