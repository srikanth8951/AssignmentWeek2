# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:52:23 2020

@author: hvsri
"""

def passwordValidityCheck(password):
    
    str1 = password
    chars = 0
    digits = 0
    symbols = 0
    
    if(len(str1)>=8 and len(str1)<=16):
        
        for i in range(0, len(str1)):
            
            ch = str1[i]
            
            if((ch>="A" and ch<="Z") or (ch>="a" and ch<="z")):
                chars = chars+1
            elif(ch>="0" and ch<="9"):
                digits = digits+1
            else:
                symbols = symbols+1
        if(chars>=1 and digits>=1 and symbols>=1):
            print("Valid Password")
        else:
            print("Invalid Password")
            
    else:
        print("Password is not in the limit")

password = input("Enter the Password: ")
passwordValidityCheck(password)