# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 15:39:10 2020

@author: hvsri
"""

def print_pattern(n): 
   
    for i in range(n): 
  
        for j in range((n // 2) + 1): 
  
            if ((j == 0 or j == n //2) and i != 0 or  i == 0 and j != 0 and j != n // 2 or i == n // 2): 
                print("*", end = "") 
            else: 
                print(" ", end = "") 
          
        print() 
      
 
# Size of the letter
num = int(input("Enter the size: \t "))
 
if num > 7:
    print_pattern(num)
else:
    print("Enter a size minumin of 8")