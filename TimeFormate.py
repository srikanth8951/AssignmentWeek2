# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 15:18:26 2020

@author: hvsri
"""

def convertTo24(str1): 
	
	if str1[-2:] == "AM" and str1[:2] == "12": 
		return "00" + str1[2:-2] 
		 
	elif str1[-2:] == "AM": 
		return str1[:-2] 
	
	elif str1[-2:] == "PM" and str1[:2] == "12": 
		return str1[:-2] 
		
	else: 
		
		return str(int(str1[:2]) + 12) + str1[2:8] 

time = input('Enter the 12 hour formate time ex(08:05:12 PM): ')
convertedTime = convertTo24(time)		 
print('Converted time in 24 hour formate is:', convertedTime) 
