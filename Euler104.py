# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 20:39:02 2016

@author: jsemko
"""

digs = '123456789'
digs = sorted(digs)

import numpy as np

phi = (1+np.sqrt(5))/2


def first_digs(n):
    full = n*np.log10(phi) - np.log10(np.sqrt(5))
    fract = full % 1
    start = np.power(10,fract)
    return int(start * 10 **8)
    
f_0 = 1
f_1 = 1
counter = 2
while True:
    last_digs = str(f_1)
    if digs == sorted(last_digs):
        print(counter)
        if sorted(str(first_digs(counter))) == digs:
            break
    f_0,f_1 = f_1, (f_0 + f_1) % 10**9
    counter +=1
        
print(counter)
