# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:30:08 2020

@author: hvsri
"""

class AcceptAndPrint:
    def __init__(self):
        self.name = ""
        
    def getter(self):
        self.name = input('Enter the name: ')
        
    def setter(self):
        print('Name which is enterd by user is: ',self.name)
    
obj = AcceptAndPrint()
obj.getter()
obj.setter()