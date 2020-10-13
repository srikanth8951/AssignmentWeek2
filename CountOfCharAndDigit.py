# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:08:02 2020

@author: hvsri
"""

def countOfCharAndDigit():
    str1 = "P@#yn26at^&i5ve"
    
    chars = 0
    digits = 0
    symbols = 0
    
    for i in range(0, len(str1)):
        
        ch = str1[i]
        
        if((ch>="A" and ch<="Z") or (ch>="a" and ch<="z")):
            chars = chars+1
        elif(ch>="0" and ch<="9"):
            digits = digits+1
        else:
            symbols = symbols+1
            
    print("Chars= ", chars)
    print("Digits= ", digits)
    print("Symbols= ", symbols)
    
countOfCharAndDigit()