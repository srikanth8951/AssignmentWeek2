# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:41:27 2020

@author: hvsri
"""

def countOfLowerCaseAndUpperCase(str1):
    
    lowerCase = 0
    upperCase = 0
    
    for i in range(0, len(str1)):
        
        ch = str1[i]
        
        if(ch>="a" and ch<="z"):
            lowerCase = lowerCase+1
            
        if(ch>="A" and ch<="Z"):
            upperCase = upperCase+1
            
    print("UpperCase= ", upperCase)
    print("LowerCase= ", lowerCase)
    
str1 = input('Enter the String: ')
countOfLowerCaseAndUpperCase(str1)