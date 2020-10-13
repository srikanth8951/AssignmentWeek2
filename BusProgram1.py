# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:04:39 2020

@author: hvsri
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