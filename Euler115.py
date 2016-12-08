# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:54:49 2016

@author: jsemko
"""
n = 200
m = 50

n_ways = dict()
for i in range(m):
    n_ways[i] = 1
n_ways[m] = 2

for i in range(m+1,n+1):
    this_step = 0
    for j in range(m,i):
        this_step += n_ways[i-j-1]
    n_ways[i] = this_step + n_ways[i-1] + 1

print(n_ways)
        