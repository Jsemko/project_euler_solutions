# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 19:55:47 2016

@author: Jeremy
"""
import numpy as np

firstterm = 0
N = 123456789


mid = N//2



prefactor = 2 ** -N

logfact = np.log(N)

for k in range(1,mid + 1):
    firstterm += np.exp( -np.log(k) + logfact)
    logfact += (np.log(N-k) - np.log(k+1))
