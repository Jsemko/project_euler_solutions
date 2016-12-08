# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 22:44:24 2016

@author: Jeremy
"""

t0 = 1
t1 = 1
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 1

num = 30
for i in range(2,num + 1):
    t00 = t0 + t1 + t2
    t10 = t0
    t20 = t1
    t30 = t3 + t4 + t5 + t6
    t40 = t3 + t6
    t50 = t4
    t60 = t0 + t1 +t2

    t0 = t00
    t1 = t10
    t2 = t20
    t3 = t30
    t4 = t40
    t5 = t50
    t6 = t60
    
print(t0 + t1 + t2 + t3 + t4 + t5 + t6)