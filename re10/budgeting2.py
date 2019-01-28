#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 18:28:25 2018

@author: laureano
"""
def comb_aux(quant,comb_list=[]):
    combs = []
    if not len(quant):
        return [comb_list]
    for idx in range(1+quant[0]):
        combs += comb_aux(quant[1:],comb_list+[idx])
    return combs

def budgeting2(budget, products, wishlist):
    wishlist = sorted(wishlist.items())
    better_comb = []
    max_budget = 0
    grid_x,grid_y = zip(*wishlist)
    comb = comb_aux(grid_y)
    values = [products[i] for i in grid_x]
    for el in comb:
        total = sum(i[0]*i[1] for i in zip(el,values))
        if total <= budget:
            if total > max_budget:
                max_budget = total
                better_comb = el
            elif total == max_budget and el > better_comb:
                better_comb = el
    return {i[0]: i[1] for i in zip(grid_x, better_comb) if i[1]!=0}

#budget = 1000
#products = {'ps4': 350, 'smartphone': 400, 'jacket': 40, 'pc': 600, 'glasses': 75}
#wishlist ={'ps4': 1, 'smartphone': 1, 'pc': 1}
#print(budgeting2(budget, products, wishlist))
#  
#budget = 1500
#products = {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}
#wishlist ={'glasses': 3, 'jeans': 2, 'pc': 1, 'xbox': 1}
#print(budgeting2(budget, products, wishlist))
#
#budget = 1000
#products = {'laptop': 2000, 'jeans': 50}
#wishlist ={'laptop': 2,'jeans': 3}
#print(budgeting2(budget, products, wishlist))
#
#budget = 1200
#products = {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}
#wishlist ={'glasses': 3, 'jeans': 2, 'pc': 1,
#'xbox':1}
#print(budgeting2(budget, products, wishlist))
#    
