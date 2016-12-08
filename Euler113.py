# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 20:31:03 2016

@author: jsemko
"""

C = list(range(1,10)[::-1])

print(C)

CC = [9]
CC.extend(C.copy())

print(CC)

dec = 100
increasing = 9
total_flat = 9
decreasing = 9

for _ in range(dec-1):
    for i in range(9):
        C[i] = sum(C[i:])
    increasing += C[0]
    
    for j in range(10):
        CC[j]= sum(CC[j:])
    decreasing += CC[0]
    
    total_flat +=9
    
    total_monotonic = increasing + decreasing - total_flat
    print(total_monotonic)


