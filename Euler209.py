# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:39:37 2016

@author: jsemko
"""
fib = {1:2,2:3}
for i in range(3,50):
    fib[i]=fib[i-1]+fib[i-2]
    
def circ(n):
    if n == 1:return 1
    if n == 2:return 3
    if n == 3:return 4
    return fib[n-1] + fib[n-3]
        


def next_step(item):
    return [item[1],item[2],item[3],item[4],item[5], int(item[0] != (item[1] and item[2]))]

import itertools

L = [list(c) for c in itertools.product([0,1],repeat = 6)]

all_cycles = []

while L:
    this_cycle = []
    this_item = L.pop()
    this_cycle.append(this_item)
    next_item = next_step(this_item)
    while L and next_item in L:
        this_cycle.append(next_item)
        L.remove(next_item)
        next_item = next_step(next_item)
    all_cycles.append(this_cycle)


n_ways = 1
for c in all_cycles:
    n_ways *= circ(len(c))
print(n_ways)
        
        
    
