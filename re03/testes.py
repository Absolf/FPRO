# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 16:54:04 2018

@author: laure
"""
'''
year_born = ("me", 1995)

normals = [ ("mom", 1976), ("sis", 2001)]

print (normals)
print (len(normals))

for name, year in normals:
    if year < 1980:
        print(name)
        '''

'''
students = [
        ("me", ["AOCO", "AMAT"]),
        ("YOU", ["fpro", "MDIS", "AMAT"])        
        ]
for name, subjects in students:
    print(name, "takes", len(subjects), "courses")
    

cont = 0;

for name, subjects in students:
    for s in subjects:
        if s == "fpro":
            cont +=1;
            
print ( "Students taking fpro IS: ", cont)
'''

'''
n = int(input("Qual valor?"))
threshold = 0.001
approximation = n/2

while True:
    better = (approximation + n/approximation)/2
    if abs(approximation - better) < threshold:
        print(better)
        break
    approximation = better'''
    
numbers = [5, 24, 88,8, 7]
cont = 0;
for number in numbers:
    cont += number % 2 == 1
    
print (cont > 0)