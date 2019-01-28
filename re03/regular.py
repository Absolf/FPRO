# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 08:26:15 2018

@author: laure
"""

import turtle;

#input of data
sides = int(input("Type the number of sides of the regular polygon: "));

size = int(input("Type the lenght of the sizes: "))

color_border = input("Color of the board: ");

color_fill = input("Color to fill the polygon: ");

#creation of window canvas & turtle
window = turtle.Screen();
window.bgcolor("white");
window.title("Regular Polygon");

regular = turtle.Turtle();
regular.hideturtle()
regular.pensize(4);
regular.color(color_border, color_fill);

regular.begin_fill();

#loop
for i in range(sides):
    regular.forward(50);
    regular.left(360/sides);
    
regular.end_fill();

window.exitonclick();