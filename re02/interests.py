# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 20:24:54 2018

@author: laure
"""



p = float(input("Principal amount: "));
r = float(input("Interest Rate: "))/100;
n = float(input("Frequency that the interest is paid out: "));
t = 2;

a = p*((1+(r/n))**(n*t));

print (a);