#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 18:05:45 2018

@author: laureano
"""

name = 'Victor Laureano Macieira Ferreira'

#print(name)
#print(name[0])
def formal(name):
    name = name.split()
    last_name = name[len(name)-1]
#    print(last_name[0])
    result =str(last_name)+", "
    teste = result
    for l in name:
#        print(l[0]+".")
        if l.istitle():
            lista_tit = l[0]
            if lista_tit == last_name[0]:
                continue
            else:
                teste +=lista_tit+". "
    return teste
        
treino = formal(name)
print(treino)
#        
#        