# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 08:35:08 2018

@author: laure
"""
import turtle
window = turtle.Screen()
window.bgcolor("white")
window.title("´Polygon")
polygon = turtle.Turtle()

# equilateral triangle

for i in range(3):
    polygon.forward(50)
    polygon.left(360/3)

# square

for i in range(4):
    polygon.forward(50)
    polygon.left(360/4)

# hexagon

for i in range(6):
    polygon.forward(50)
    polygon.left(360/6)

#octogon

for i in range(8):
   polygon.forward(50)
   polygon.left(360/8)

window.exitonclick()