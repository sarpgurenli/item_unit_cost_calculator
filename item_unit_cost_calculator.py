# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 22:38:27 2018

@author: sarpg
"""

import numpy as np
def item_calculator(x):#function
    s = np.linalg.solve(boxes, totals)# cost calculator
    k = int(s[x])#value transform to integer type
    return k
boxes = np.array([ 
            [3, 5, 0],
            [0, 3, 6],
            [3, 0, 5]
                     ])#box array for 3 box
totals = np.array([
            [46],
            [75],
            [71]
            ])# total amount prices for 3 box
print("Unit Cost of pipe elbows: {}TL".format(item_calculator(0)))# print unit Cost of pipe elbows
print("Unit Cost of electrodes: {}TL".format(item_calculator(1)))# print unit Cost of electrodes
print("Unit Cost of pipe tees: {}TL".format(item_calculator(2)))# print unit Cost of pipe tees