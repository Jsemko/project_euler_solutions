# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 19:25:37 2016

@author: Jeremy
"""

import numpy as np


values = np.arange(1,21)
doublevalues = values * 2
triplevalues = values * 3


allvalues = np.concatenate((np.array([0]), values, doublevalues, triplevalues, np.array([25,50])))

counts= dict()

for i in range(allvalues.size):
    for j in range(i,allvalues.size):
        if allvalues[i]+allvalues[j] in counts:
            counts[allvalues[i]+allvalues[j]] +=1
        else:
            counts[allvalues[i]+allvalues[j]] = 1
        
        
print(counts)


under = 171

alldoubles = np.concatenate((doublevalues,[50]))

totalcount = 0

for i in range(2,100):
    for k in alldoubles:
        newtarget = i - k
        if newtarget in counts:
            totalcount += counts[newtarget]
            
print(totalcount)