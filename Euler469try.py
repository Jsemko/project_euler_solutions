# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 13:47:11 2016

@author: Jeremy
"""

ans = { 0: 0,
       1:0,
       2:1,
       3:4/3
       }
       
for i in range(4,200):
    tempsum = -1
    for j in range(1,i-1):
        tempsum+=ans[j]
    ans[i]=2 + (2/i)*tempsum
    

a0 = 0
a1 = 0
for i in range(2,300000000):
    tmp = a1
    a1 = (i-1)/i * a1 + (2/i)*a0 + 2/i
    a0 = tmp

a0 = 0
a1 = 1
for i in range(3,300000000):
    tmp = a1
    a1 = a1 + a0 * (2/(i-2)) + 2
    a0 = tmp
import numpy as np

a =(10**18 - 3 + 1)/2 * (np.exp(-2) + 1)  + np.exp(-2) - 1

b = (a + 2)/ (10 ** 18)

ans = {1:1,
       2:2}
       
for i in range(3,30):
    tmpsum = 0
    for j in range(1,i-1):
        tmpsum += ans[j]
    ans[i] = 2/(i-2) * tmpsum
    print(i,ans[i-1]/i)