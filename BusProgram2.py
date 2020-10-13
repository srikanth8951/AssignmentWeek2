# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 22:25:06 2020

@author: hvsri
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