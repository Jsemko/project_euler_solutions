# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 21:34:45 2016

@author: Jeremy
"""

a = list(range(2,100000001))
b = list(range(2,100000001))
current = 1
totalsum = 0

for i in range(10000):
    current *= a[i]
    j = 0
    while j < len(b) and b[j] < current:
        if current % b[j] ==0:
            totalsum += a[i]
            del b[j]
        else:j+=1       
        
print(totalsum)