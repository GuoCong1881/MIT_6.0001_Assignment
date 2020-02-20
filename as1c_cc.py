# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:01:19 2020

@author: guoco
"""
import math
annual_salary = float(input("Enter your annual salary: "))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04


def save(annual_salary, portion_saved):
    current_savings = 0
    for i in range (1, 37):
        current_savings += current_savings*r/12 + annual_salary/12 * portion_saved/10000
        j = i % 6
        if j == 0:
            annual_salary = annual_salary * (1 + semi_annual_raise)
    return current_savings            

def portion(annual_salary):
    top = 10000
    low = 0
    portion_saved = int((top + low)/2)
    j = 0
    while abs(total_cost * portion_down_payment - save(annual_salary, portion_saved)) >= 100 and j <= math.log2(10000):
        portion_saved = int((top + low)/2)
        if total_cost * portion_down_payment > save(annual_salary, portion_saved):
            low = portion_saved
        else:
            top = portion_saved
        j = j + 1
    if j > math.log2(10000):
        print ("It is not possible to pay the down payment in three years")
    else:
        print("Best savings rate: ", portion_saved/10000)
        print("Steps in bisection search: ", j)
    return portion_saved
    
portion(annual_salary)
#print ("Best savings rate ", portion/10000)