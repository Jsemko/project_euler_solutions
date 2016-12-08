lim = 45

import time

pl = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]

pl = [p for p in pl if p <=lim]

import math as m

n = [int(m.log(lim)/m.log(p)) for p in pl]

a=[p**nn for p,nn in zip(pl,n)]

p = 1
for e in a:
    p*=e

rem = [p**2 // i**2 for i in range(2,lim+1)]

target_p = p**2 // 2


def count_it(a_list,target):
    if target == 0:return 1
    #if len(a_list)==1 and target == a_list[0]:
    #    return 1
    i = 0
    add_on = 0
    while i < len(a_list)-1 and sum(a_list[i:])>= target:
        if a_list[i] <= target:
            add_on += count_it(a_list[i+1:],target-a_list[i])
        i+=1
    if a_list[-1] == target:
        add_on+=1
    return add_on

t0 = time.time()
print(count_it(rem,target_p))
print('took %.2f' % (time.time() - t0))
