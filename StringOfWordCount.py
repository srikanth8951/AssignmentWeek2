# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:28:27 2020

@author: hvsri
"""

def procedure(string,target):
    words=string.split(" ") 
    solution=[] 
    for i in range(len(words)):
        if words[i]==target: 
            solution.append(i)
    if len(solution)==0: 
        return False
    return solution

string="we dont need no education we dont need no thought control no we dont"
print (procedure(string, "dont"))




