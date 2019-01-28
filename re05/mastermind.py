# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 01:50:50 2018

@author: laure
"""


def mastermind(g1, g2, g3, c1, c2, c3):
    '''
    g1 = input("g1: ")
    g2 = input("g1: ")
    g3 = input("g1: ")
    
    c1 = input("c1: ")
    c2 = input("c2: ")
    c3 = input("c3: ")
    '''
    elements = [g1, g2, g3, c1, c2, c3]
    points = 0;
    for i in range(len(elements)):
        #main cases
        if g1 == c1:
            points += 3
        if g2 == c2:
            points += 3
        if g3 == c3:
            points += 3
        #other cases
        elif g1 == c2 or g1 == c3:
            points += 1
        elif g2 == c1 or g2 == c3:
            points += 1
        if g3 == c1 or g3 == c2:
            points += 1
      
        return points



game = mastermind(guess1, guess2, guess3, check1, check2, check3)

print(game)