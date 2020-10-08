# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 20:11:18 2020

@author: hvsri
"""

"""
 Queston1: Given a two integer numbers return their 
product and if the product is greater than 1000, then return their sum """""

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

"""###########################"""

""" 
Question 2: Reverse a given number and return true if it is the same as the original number

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

"""###########################"""

"""
Question 3: Count all lower case, upper case, digits, and special symbols from a given string

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

"""###########################"""

""" 
Question 4: Class Inheritance

"""

class Vehicle:

    def __init__(self, name, max_speed, mileage):

        self.name = name

        self.max_speed = max_speed

        self.mileage = mileage

 

    def seating_capacity(self, capacity):

        return f"The seating capacity of a {self.name} is {capacity} passengers"
       
class Bus(Vehicle):
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
    
bus = Bus("bus", 80, 30)
print(bus.seating_capacity(50))

"""###########################"""

"""
Question 5: Class Inheritance

"""

class Vehicle:

    def __init__(self, name, mileage, capacity):

        self.name = name

        self.mileage = mileage

        self.capacity = capacity

    def fare(self):

        return self.capacity * 100

class Bus(Vehicle):

    def fare(self):
        total_fare = self.capacity*100
        final_amount = total_fare+(total_fare*(10/100))
        return final_amount

School_bus = Bus("School Volvo", 12, 50)

print("Total Bus fare is:", School_bus.fare())

"""###########################"""

"""

Question 6. Write a Python program to check the validity of password input by users. 

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

"""###########################"""

"""
Question 7 . Write a Python program to print alphabet pattern 'A'

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

"""###########################"""

"""
Write a Python program to display a number with a comma separator.

"""
num = int(input('Enter the Number'))
print("Original Number: ", num)
print("Number with comma separator: "+"{:,}".format(num));

"""###########################"""

"""
Question 9. Write a Python program to display astrological sign for given date of birth. 

"""

def astroSign(day, month):
    if month == 'december':
    	astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 'january':
    	astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month == 'february':
    	astro_sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month == 'march':
    	astro_sign = 'Pisces' if (day < 21) else 'aries'
    elif month == 'april':
    	astro_sign = 'Aries' if (day < 20) else 'taurus'
    elif month == 'may':
    	astro_sign = 'Taurus' if (day < 21) else 'gemini'
    elif month == 'june':
    	astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month == 'july':
    	astro_sign = 'Cancer' if (day < 23) else 'leo'
    elif month == 'august':
    	astro_sign = 'Leo' if (day < 23) else 'virgo'
    elif month == 'september':
    	astro_sign = 'Virgo' if (day < 23) else 'libra'
    elif month == 'october':
    	astro_sign = 'Libra' if (day < 23) else 'scorpio'
    elif month == 'november':
    	astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
    print("Your Astrological sign is :",astro_sign)

day = int(input('Input Birthday: '))
month = input("Input month of birth (e.g. march, july etc): ")
astroSign(day, month)

"""###########################"""

"""
Question 10.Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

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

"""###########################"""

"""
Question 11   Print with your own font using Python !!

"""
def ownPattern(str1):
    lngth = len(str1)  
    
    for x in range(0, lngth): 
    	c = str1[x] 
    	c = c.upper() 
    	
    	if (c == "A"): 
    		print("..######..\n..#....#..\n..######..", end = " ") 
    		print("\n..#....#..\n..#....#..\n\n") 
    		
    	elif (c == "B"): 
    		print("..######..\n..#....#..\n..#####...", end = " ") 
    		print("\n..#....#..\n..######..\n\n") 
    		
    	elif (c == "C"): 
    		print("..######..\n..#.......\n..#.......", end = " ") 
    		print("\n..#.......\n..######..\n\n") 
    		
    	elif (c == "D"): 
    		print("..#####...\n..#....#..\n..#....#..", end = " ") 
    		print("\n..#....#..\n..#####...\n\n") 
    		
    	elif (c == "E"): 
    		print("..######..\n..#.......\n..#####...", end = " ") 
    		print("\n..#.......\n..######..\n\n") 
    		
    	elif (c == "F"): 
    		print("..######..\n..#.......\n..#####...", end = " ") 
    		print("\n..#.......\n..#.......\n\n") 
    		
    	elif (c == "G"): 
    		print("..######..\n..#.......\n..#.####..", end = " ") 
    		print("\n..#....#..\n..#####...\n\n") 
    		
    	elif (c == "H"): 
    		print("..#....#..\n..#....#..\n..######..", end = " ") 
    		print("\n..#....#..\n..#....#..\n\n") 
    		
    	elif (c == "I"): 
    		print("..######..\n....##....\n....##....", end = " ") 
    		print("\n....##....\n..######..\n\n") 
    		
    	elif (c == "J"): 
    		print("..######..\n....##....\n....##....", end = " ") 
    		print("\n..#.##....\n..####....\n\n") 
    		
    	elif (c == "K"): 
    		print("..#...#...\n..#..#....\n..##......", end = " ") 
    		print("\n..#..#....\n..#...#...\n\n") 
    		
    	elif (c == "L"): 
    		print("..#.......\n..#.......\n..#.......", end = " ") 
    		print("\n..#.......\n..######..\n\n") 
    		
    	elif (c == "M"): 
    		print("..#....#..\n..##..##..\n..#.##.#..", end = " ") 
    		print("\n..#....#..\n..#....#..\n\n") 
    		
    	elif (c == "N"): 
    		print("..#....#..\n..##...#..\n..#.#..#..", end = " ") 
    		print("\n..#..#.#..\n..#...##..\n\n") 
		
    	elif (c == "O"): 
    		print("..######..\n..#....#..\n..#....#..", end = " ") 
    		print("\n..#....#..\n..######..\n\n") 
    		
    	elif (c == "P"): 
    		print("..######..\n..#....#..\n..######..", end = " ") 
    		print("\n..#.......\n..#.......\n\n") 
    		
    	elif (c == "Q"): 
    		print("..######..\n..#....#..\n..#.#..#..", end = " ") 
    		print("\n..#..#.#..\n..######..\n\n") 
    		
    	elif (c == "R"): 
    		print("..######..\n..#....#..\n..#.##...", end = " ") 
    		print("\n..#...#...\n..#....#..\n\n") 
    		
    	elif (c == "S"): 
    		print("..######..\n..#.......\n..######..", end = " ") 
    		print("\n.......#..\n..######..\n\n") 
    		
    	elif (c == "T"): 
    		print("..######..\n....##....\n....##....", end = " ") 
    		print("\n....##....\n....##....\n\n") 
    		
    	elif (c == "U"): 
    		print("..#....#..\n..#....#..\n..#....#..", end = " ") 
    		print("\n..#....#..\n..######..\n\n") 
    		
    	elif (c == "V"): 
    		print("..#....#..\n..#....#..\n..#....#..", end = " ") 
    		print("\n...#..#...\n....##....\n\n") 
    		
    	elif (c == "W"): 
    		print("..#....#..\n..#....#..\n..#.##.#..", end = " ") 
    		print("\n..##..##..\n..#....#..\n\n") 
    		
    	elif (c == "X"): 
    		print("..#....#..\n...#..#...\n....##....", end = " ") 
    		print("\n...#..#...\n..#....#..\n\n") 
    		
    	elif (c == "Y"): 
    		print("..#....#..\n...#..#...\n....##....", end = " ") 
    		print("\n....##....\n....##....\n\n") 
    		
    	elif (c == "Z"): 
    		print("..######..\n......#...\n.....#....", end = " ") 
    		print("\n....#.....\n..######..\n\n") 
    		
    	elif (c == " "): 
    		print("..........\n..........\n..........", end = " ") 
    		print("\n..........\n\n") 
    		
    	elif (c == "."): 
    		print("----..----\n\n") 
        
print('Enter the String')
str1 = input()
ownPattern(str1)

"""###########################"""

"""
Python program to convert time from 12 hours to 24-hour format

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

"""###########################"""

"""
Question 13 Generating random strings until a given string is generated

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

"""###########################"""

"""
Question 14.Python Program to Create a Class in which One Method Accepts a String from the User and Another print it

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

"""###########################"""

"""
Question 15 Define a class which has at least two metho

"""
class getAndSet:
    def __init__(self):
        self.name = ""
        
    def getString(self):
        string = input('Enter a name: ')
        self.name = string
        
    def printString(self):
        print(self.name.upper)
        
obj = getAndSet()
obj.getString()
obj.printString()

"""###########################"""

"""
Question 17 Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

"""

number = input("Enter value: ")

n1 = number * 1
n2 = number * 2
n3 = number * 3
n4 = number * 4

total = int(n1) + int(n2) + int(n3) + int(n4)
print(total)

"""###########################"""


