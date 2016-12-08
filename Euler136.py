import numpy as np
import math

total_ans = np.zeros(50000001,dtype=np.int32)

for C in range(1,12248):   #so that final answer in positive integers
    if C % 2 ==0 :print(C)
    B_start = -C//3 + 1
    if B_start*2 == C:
        B_start+=1
    if (C + B_start) % 2 == 1:
        B_start+=1
    B_last = math.floor((5e7/C - C)/2)
    for B in range(B_start,B_last+1,2):
        n = C*(2*B+C)
        total_ans[n] +=1


print(total_ans[:20])
print(np.sum(total_ans[1:]==1))
