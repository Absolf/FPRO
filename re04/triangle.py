# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 20:30:49 2018

@author: laure
"""

#triangulos = ["Equilateral", "Isosceles", "Scalene"]



def triangle_type():
    result = "Not implemented yet"
    lado_a = int(input("lado a ? "))
    lado_b = int(input("lado b ? "))
    lado_c = int(input("lado c ? "))
    if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_b + lado_c > lado_a:
        if lado_a == lado_b and lado_b == lado_c:
            result = 'Equilateral'
        elif lado_a == lado_b or lado_b == lado_c or lado_a == lado_c:
            result = 'Isoceles'
        else:
            result = 'Scalene'
    else:
        result = 'Not a triangle'
    return result

print(triangle_type())