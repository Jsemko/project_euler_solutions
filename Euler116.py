# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:21:29 2016

@author: jsemko
"""

def combos(total,l):
    array = [0] * (total+1)
    for i in range(1,l):array[i] = 0
    array[l]=1
    for i in range(l+1,total+1):
        array[i] = array[i-l] + array[i-1] + 1
    return array[-1]
    
print(combos(50,2) + combos(50,3) + combos(50,4))