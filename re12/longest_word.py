#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:35:17 2018

@author: laureano
"""
import urllib.request
def longest_word(url):
    with open('words','r') as f:   
        response = urllib.request.urlopen(url)
        html = response.read().decode()
        url_w = set(html.split())
        
        word = f.read()
        url_verify_w = set(word.split())
        
        intersec = url_w.intersection(url_verify_w)
     
        return sorted(intersec, key = lambda w:len(w))[-1]
#print(longest_word("​https://en.wikipedia.org/wiki/Monty_Python​"))