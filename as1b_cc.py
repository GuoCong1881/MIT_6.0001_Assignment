# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 17:33:03 2020

@author: guoco
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ."))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: ."))


def time(annual_salary, portion_saved, total_cost, semi_annual_raise):
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    i = 0
    while current_savings < total_cost * portion_down_payment:
        current_savings += current_savings*r/12 + annual_salary/1200 * portion_saved
        i = i+1
        j = i % 6
        if j == 0:
            annual_salary = annual_salary * (1+semi_annual_raise/100) 
    return i
    
m = time(annual_salary, portion_saved, total_cost, semi_annual_raise)
print ("Number of months: ", m)