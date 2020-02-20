# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 15:44:46 2020

@author: guoco
"""
import numpy as np
x = int (input ("Enter number x: "))
y = int (input ("Enter number y: "))
a = x**y
b = np.log2(x)
print ("x ^ y = ", a)
print ("log(x) = ", b)
print (2**b)