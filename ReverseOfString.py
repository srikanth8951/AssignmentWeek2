# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:13:01 2020

@author: hvsri
"""



def reverse(str1):
    print(str1)
    if len(str1) == 0:
        return str1
    else:
        return reverse(str1[1:]) + str1[0] 


str1 = input("Enter the string to be reversed: ")

print("The Given String  is: ", str1)

print("Reversed String is: ", reverse(str1))

 

