# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 22:34:58 2016

@author: jsemko
"""

def max_r(n):
    M = 2*n
    mod = n**2
    for i in range(1,n):
        N = 2*i*n % mod
        if N > M:
            M = N
    return M
    
print(max_r(7))

total = 0

for i in range(3,1001):
    total += max_r(i)
    
print(total)