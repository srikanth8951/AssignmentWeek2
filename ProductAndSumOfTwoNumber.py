# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:30:24 2020

@author: hvsri
"""

def productOfTwoNumber():
    number1 = int(input("Enter the number: "))
    number2 = int(input("Enter the number: "))
    
    result = number1*number2
    sumOfTwoNumber = number1+number2
    
    if(result>1000):
        return sumOfTwoNumber
    else:
        return result
    
result = productOfTwoNumber()
print(result)