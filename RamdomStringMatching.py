# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:08:38 2020

@author: hvsri
"""

 

import random 

def randomString():
    char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    name = input("Enter your target text: ")
    string1 = ''.join(random.choice(char)	for i in range(len(name))) 
    string2 = '' 
    
    flag = False
    i = 0
    
    while flag == False: 
    	print(string1) 
    	
    	string2 = '' 
    	flag = True
    	
    	for j in range(len(name)): 
    		if string1[j] != name[j]: 
    			flag = False
    			string2 += random.choice(char) 
    		else: 
    			string2 += name[j] 
    			
    	i += 1
    	string1 = string2
    
    print("String is matched after " + str(i) + " times") 
randomString()