# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:54:49 2016

@author: jsemko
"""

n_ways = {0 : 1, 1:1,2:1,3:2}

for i in range(4,51):
    this_step = 0
    for j in range(3,i):
        this_step += n_ways[i-j-1]
    n_ways[i] = this_step + n_ways[i-1] + 1

print(n_ways)
        