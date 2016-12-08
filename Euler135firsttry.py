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
primelist = primes_under(int(1000000**.5) + 1)




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

from collections import Counter
import itertools

def get_factors(pf):
    pf = Counter(pf)
    pairs = [(p,pf[p]) for p in pf]
    def get_all_them(list_of_primes):
        p, m = list_of_primes[0]
        new_list = [p ** i for i in range(m + 1)]
        if len(list_of_primes)==1:
            return new_list
        return [a*b for a,b in itertools.product(new_list,get_all_them(list_of_primes[1:]))]
    return get_all_them(pairs)



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

prime_factor_dict = dict()

total_count = 0

for n in range(5,1000000):
    addon = get_factors(prime_factor(n))
    addon = [i for i in addon if i**2 < 3*n]
    if len(addon) >=10:
        curcount = 0
        for c in addon:
            TB = (n // c) - c
            if TB % 2 == 0:
                B = TB //2
                if (B+c) % 2 == 0:
                    curcount+=1
        if curcount ==10:
            total_count+=1
            print(n)
    if (n % 100000) ==1:print(n)

print(total_count)


