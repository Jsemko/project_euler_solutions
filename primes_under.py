def primes_under(m):
    primes = [2]
    for i in range(3,m,2):
        if (i + 1)% 100000 == 0: print('done ' + str(i))
        j = 0
        lim = int(i**.5) + 1
        while lim > primes[j]:
            if i % primes[j] == 0: break
            j+=1
        else: primes.append(i)
    return primes

import time
t = time.time()
primelist = primes_under(100000)
print('Took {s} secs'.format(s = time.time() - t))

print(primelist[:5])

def alt_prime(m):
    primes = list(range(2,m))
    cur = 0
    while cur < len(primes):
        p = primes[cur]
        start = cur + 1
        while start < len(primes):
            if primes[start] % p == 0:
                del primes[start]
            else:
                start+=1
        cur +=1
    return primes
t = time.time()
primelist2 = alt_prime(100000)
print('Took {s} secs'.format(s = time.time() - t))


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


