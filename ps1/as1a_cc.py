# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:57:45 2020

@author: guoco
"""
#Part A: House Hunting
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: ."))
total_cost = float(input("Enter the cost of your dream home: "))

def time(annual_salary, portion_saved, total_cost):
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    i = 0
    while current_savings < total_cost * portion_down_payment:
        current_savings += current_savings*r/12 + annual_salary/1200 * portion_saved
        i = i+1
    return i
    
m = time(annual_salary, portion_saved, total_cost)
print ("Number of months: ", m)


