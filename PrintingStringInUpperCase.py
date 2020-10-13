# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:31:57 2020

@author: hvsri
"""

class getAndSet:
    def __init__(self):
        self.name = ""
        
    def getString(self):
        string = input('Enter a name: ')
        self.name = string
        
    def printString(self):
        print(self.name.upper)
        
obj = getAndSet()
obj.getString()
obj.printString()
         