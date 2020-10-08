# AssignmentWeek2
Question 1: Given a two integer numbers return their product and if the product is greater than 1000, then return their sum

Given:

number1 = 20

number2 = 30

Expected Output:

The result is 600

Given:

number1 = 40

number2 = 30

Expected Output:

The result is 70

 

Question 2: Reverse a given number and return true if it is the same as the original number

Expected Output:

original number 121

The original and reverse number is the same

original number 125

The original and reverse number is not same

 

Question 3: Count all lower case, upper case, digits, and special symbols from a given string

Given:

str1 = "P@#yn26at^&i5ve"

Expected Outcome:

Total counts of chars, digits,and symbols

Chars = 8

Digits = 3

Symbol = 4

 

Question 4: Class Inheritance

Given:

Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

Use the following code for your parent Vehicle class. You need to use method overriding.

class Vehicle:

    def __init__(self, name, max_speed, mileage):

        self.name = name

        self.max_speed = max_speed

        self.mileage = mileage

 

    def seating_capacity(self, capacity):

        return f"The seating capacity of a {self.name} is {capacity} passengers"

Expected Output:

The seating capacity of a bus is 50 passengers

 

Question 5: Class Inheritance

Given:

Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of the total fare.

Note: The bus seating capacity is 50. so the final fare amount should be 5550. You need to override the fare() method of a Vehicle class in Bus class.

Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.

class Vehicle:

    def __init__(self, name, mileage, capacity):

        self.name = name

        self.mileage = mileage

        self.capacity = capacity

    def fare(self):

        return self.capacity * 100

class Bus(Vehicle):

    pass

School_bus = Bus("School Volvo", 12, 50)

print("Total Bus fare is:", School_bus.fare())

Expected Output:

Total Bus fare is: 5500.0

 

Question 6. Write a Python program to check the validity of password input by users. 

At least 1 letter between [a-z] and 1 letter between [A-Z].

At least 1 number between [0-9].

At least 1 character from [$#@].

Minimum length of 6 characters.

The maximum length of 16 characters.

Question 7 . Write a Python program to print alphabet pattern 'A'

 

Question 8. Write a Python program to display a number with a comma separator.

Question 9. Write a Python program to display astrological sign for given date of birth. 
Expected Output:

Input birthday: 15
Input month of birth (e.g. march, july etc): may
Your Astrological sign is : Taurus 

 

Each number is the two numbers above it added together

Question 10. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

Question 11   Print with your own font using Python !!

Question 12 Python program to convert time from 12 hours to 24-hour format

Question 13 Generating random strings until a given string is generated

Question 14. Python Program to Create a Class in which One Method Accepts a String from the User and Another print it

Question 15 Define a class which has at least two methods:

getString: to get a string from console input

printString: to print the string in upper case.

Also please include a simple test function to test the class methods.

Question:16 Write a program that takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.

            Note: i=0,1.., X-1; j=0,1,¡¬Y-1.

            Example

            Suppose the following inputs are given to the program:

            3,5

            Then, the output of the program should be:

            [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Question 17 Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

Suppose the following input is supplied to the program:

9

Then, the output should be:

11106

Question 18 Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

D 100

W 200

D means deposit while W means withdrawal.

Suppose the following input is supplied to the program:

D 300

D 300

W 200

D 100

Then, the output should be:

500

 Question 19    A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

            UP 5

            DOWN 3

            LEFT 3

            RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.

            Example:

            If the following tuples are given as input to the program:

            UP 5

            DOWN 3

            LEFT 3

            RIGHT 2

            Then, the output of the program should be:

            2

Question 20: Implemented a Tic Tac Toe Game and write the complete Explanation
