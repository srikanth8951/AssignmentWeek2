# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:35:06 2020

@author: hvsri
"""

def reverseOfNumber():
    num1 =  int(input("Enter the number: "))
    org_num = num1
    rev_num = 0
    
    while(num1>0):
        rev_num = rev_num*10+num1%10
        num1 = num1//10
    
    if(rev_num == org_num):
        print(rev_num)
        return True
    else:
        print(rev_num)
        return False
result = reverseOfNumber()
print(result)