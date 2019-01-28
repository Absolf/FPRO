# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:27:07 2018

@author: laure
"""

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")

turtle = turtle.Pen()
turtle.shape('turtle')
turtle.color('blue')
turtle.stamp()
turtle.pensize(3)

#distance between each turtle (degrees to turn)
steps=30

#loop
for i in range(12):
     turtle.penup()
     turtle.forward(85)
     turtle.pendown()
     turtle.forward(14)
     turtle.penup()
     turtle.forward(12)
     turtle.stamp()
     turtle.home()
     turtle.right(steps)
     steps += 30
  
window.exitonclick()
