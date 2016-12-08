def primes_under(m):
    primes = [2]
    for i in range(3,m,2):
        if (i + 1)% 100000 == 0: print('done ' + str(i))
        j = 0
        while j < len(primes) and i >= primes[j]**2:
            if i % primes[j] == 0: break
            j+=1
        else: primes.append(i)
    return primes
primelist = primes_under(int(10000000000 ** .5) + 1)





def prime_factor(n):
    l = len(primelist)
    i = 0
    factor = []
    while n > 1 and i < l:
        if n % primelist[i] == 0:
            n //= primelist[i]
            factor.append(primelist[i])
        else:
            i+=1
    if factor:
        if n > 1:factor.append(n)
        return factor
    else: return [n]



def fund(n):
    f = prime_factor(n)
    c = Counter(f)
    return [c[i] for i in c]



def get_n_solutions(l):
    amt = l[0]+1
    for n in l[1:]:
        amt += (2*amt -1)*n
    return amt


c = 0

import itertools

import numpy as np
primelist = np.array([2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])

minnum = 17**20

print(minnum)
print(prime_factor(9350130049860600))

for i in range(1,5):
    for j in range(1,i+1):
        for k in range(1,j+1):
            for l in range(1,k+1):
                for m in range(1,l+1):
                    for c in itertools.product([0,1,2],repeat=10):
                        start = [i,j,k,l,m]
                        start.extend(list(c))
                        if not sorted(start) == start[::-1]:continue
                        sol = 1
                        for ii in range(15):
                            sol*= int(2*start[ii] + 1)
                        sol += 1
                        sol //= 2
                        if sol < 0:print('oops')
                        if sol > 4000000:
                            num = 1
                            for ii in range(15):
                                num*= int(primelist[ii]) ** int(start[ii])
                            if num < minnum:
                                minnum=num
                                print(num)

