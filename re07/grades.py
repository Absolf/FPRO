#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:33:01 2018

@author: laureano
"""

def sort_grades(records):
        
    return  tuple(sorted(records, key=lambda records: (-sum(records[2])/len(records[2]),records[0],records[1])))

records=(('João', 'up20186042', (90, 87)),
('Ana', 'up20186040', (90, 90)),
('José', 'up20186063', (70, 90)),
('Ana', 'up20186061', (90, 90)),
('Tiago', 'up20186070', (100, 90)))
print(sort_grades(records))