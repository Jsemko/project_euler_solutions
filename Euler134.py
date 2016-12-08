import numpy as np

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
primelist = primes_under(int(1000000) + 10000)

print(primelist[-1])


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




def is_prime(n):
    if n ==1:return False
    if n ==2: return True
    top = n**.5 + 1
    l = len(primelist)
    i = 0
    cur_prime = primelist[i]
    while i < l and cur_prime <= top:
        if n % cur_prime == 0:
            return False
        i+=1
        cur_prime = primelist[i]
    return True


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = 1
    for nn in n:
        prod*= nn

    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

s=0
for i in range(len(primelist)):
    p1 = primelist[i]
    if p1 <4:continue
    if p1 >1e6:break
    p2 = primelist[i+1]
    d = int(np.log10(p1))+1
    n = chinese_remainder([10**d,p2],[p1,0])
    if p1==19:print(n)
    s+=n
print(s)


