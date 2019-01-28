# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 02:31:25 2018

@author: laure
"""
def get_positions(word_list, sentence):
    solution =""
    
    for word1 in range(len(word_list)):
        for word2 in range(len(word_list)):
            if word1 != word2:
                if word_list[word1] + " " + word_list[word2] == sentence:
                    solution = str(word1) + " " + str(word2)
                
            
    return solution


print(get_positions(["hello", "brave", "world"], "hello world"))
print(get_positions(["hello", "lousy", "world"], "lousy world"))
print(get_positions(["hello", "world", "lousy"], "lousy world"))
print(get_positions(["hello", "brave", "hello"], "hello hello"))
