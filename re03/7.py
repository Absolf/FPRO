# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 18:02:28 2018

@author: laure
"""

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]

import turtle

drunkPirate = turtle.Turtle()

drunkPirate.shape("triangle")
drunkPirate.color("azure1","Red")

window = turtle.Screen()

drunkPirate.penup()
drunkPirate.forward(60)

drunkPirate.pendown()

for t in turns:
    drunkPirate.forward(100)
    drunkPirate.left(t)

print("Final heading was: ", drunkPirate.heading())

window.exitonclick()