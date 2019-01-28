#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 12:18:25 2018

@author: laureano
"""

def budgeting(budget, products, wishlist):
    def cost(products, wishlist):
        real_cost = 0
        for item in products:
    #        print(item)
            if item in wishlist:
                real_cost += products[item] * wishlist[item]
        return real_cost
    
    while cost(products, wishlist)> budget:
        lower = lowerPrice(products,wishlist)
        if wishlist[lower] > 1:
            wishlist[lower] -=1
        else:
            del wishlist[lower]
    return wishlist

def lowerPrice(products, wishlist):
    cheaper = 99999999999999999999999
    product = None 
    for item in products:
        if products[item] < cheaper and item in wishlist:
            cheaper = products[item]
            product = item
    return product


    

    
    
budget = 1500
products = {'xbox': 250, 'smartphone': 500, 'jeans': 50,
'pc': 600, 'glasses': 100}
wishlist ={'glasses': 3, 'jeans': 2, 'pc': 1,
'xbox':1}
print(budgeting(budget, products, wishlist))

#budget = 1000
#products = {'ps4': 350, 'smartphone': 400, 'jacket': 40,
#'pc': 600, 'glasses': 75}
#wishlist ={'ps4': 1, 'smartphone': 1, 'pc': 1}
#print(budgeting(budget, products, wishlist))

#budget = 1200
#products = {'xbox': 250, 'smartphone': 500, 'jeans': 50, 'pc': 600, 'glasses': 100}
#wishlist ={'glasses': 3, 'jeans': 2, 'pc': 1,
#'xbox':1}
#print(budgeting(budget, products, wishlist))
    
#budget = 750
#products = {'nintendo': 100, 'mouse': 20, 'hoodie': 45, 'backpack': 30, 'tv': 300}
#wishlist ={'nintendo': 1, 'mouse': 1, 'hoodie': 4, 'tv': 2}
#print(budgeting(budget, products, wishlist))
#print(lowerPrice(products,wishlist))