#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 14:28:56 2018

@author: laureano
"""
def file_finder(dirs, file_name):
    if file_name in dirs and file_name !=dirs[0]:
        return f"{dirs[0]}/{file_name}"
    else:
        for el in dirs: 
            if isinstance(el, list):
                result = file_finder(el, file_name)
                if result:
                    return "{0}/{1}".format(dirs[0],result)

dirs = ["home",
          ["Documents",
             [ "FPRO", "lists.txt", "recursion.pdf", "functions" ],
             [ "Python", "hello_world.py", "readme.md" ],
          ],
          ["Downloads",
             [ "Movies",
                [ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],
                "1.avi", "22", "001.mp4"
             ],
          ],
          "tmp.txt", "page.html"
       ]
             
#print(file_finder(dirs,'Documents'))