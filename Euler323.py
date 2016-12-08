# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 22:14:12 2016

@author: Jeremy
"""

import numpy as np

def fact(n):
    if n==0: return 1
    return n*fact(n-1)


def nchoosek(n,k):
    return round(fact(n)/(fact(n-k)*fact(k)))

thelist = [0]

for i in range(1,33):
    thelist.append(2**i)
    for j in range(i):    
        thelist[i] += thelist[j] * nchoosek(i,j)
    thelist[i] /= (2 ** i -1)
