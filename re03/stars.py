# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 18:40:09 2018

@author: laure
"""

import turtle
window = turtle.Screen()
window.bgcolor("blue")

turtle = turtle.Pen()
turtle.shape('circle')
turtle.color('white')
turtle.pensize(3)
turtle.stamp()

star_sizes = int(input("type the star size: "))
star_steps = 360/star_sizes
steps_aux = star_steps

#loop
for i in range(star_sizes):
     turtle.pendown()
     turtle.forward(100)
     turtle.stamp()
     turtle.home()
     turtle.right(steps_aux)
     steps_aux += star_steps;
     
window.exitonclick()
