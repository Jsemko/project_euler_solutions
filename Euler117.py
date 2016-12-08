# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 21:21:29 2016

@author: jsemko
"""



def combos(total):
    array = [0] * (total+1)
    array[1] = 1
    array[2] = 2
    array[3] = 4
    array[4] = 8
    for i in range(5,total+1):
        array[i] = array[i-2] + array[i-3] + array[i-4] + array[i-1]
    return array[-1]
    
print(combos(50))
    
