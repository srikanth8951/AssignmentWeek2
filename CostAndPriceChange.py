# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 20:15:38 2020

@author: hvsri
"""

def pay_change(paid, cost):
   
    change = paid - cost
    result = {}


    n_twenty = change // 20
    result['$20'] = n_twenty
    rest = change % 20

    n_ten = rest // 10
    result['$10'] = n_ten
    rest = rest % 10

    n_five = rest // 5
    result['$5'] = n_five
    rest = rest % 5

    n_two = rest // 2
    result['$2'] = n_two
    rest = rest % 2

    n_one = rest // 1
    result['$1'] = n_one

 
    for k, v in result.items():
        if v != 0:
            print('Need', v, 'bills of', k)

paid = int(input('Enter the amount paid: '))
cost = int(input('Enter the cost of item: '))            
pay_change(paid, cost)