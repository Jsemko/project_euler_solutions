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
primelist = primes_under(int(1000000000 ** .5) + 1)

print(primelist[-1])


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

small_primelist = [p for p in primelist if len(set(str(p)))==len(str(p)) and p < 10000]

import itertools


def count_full_primes(start,digits):
    c = 0
    for perm in itertools.permutations(digits):
        n = int(''.join(perm))
        if n >= start and is_prime(n):
            print(n)
            c+=1
    return c


def get_n_partitions(pl, digits):
    if not pl:
        M = 10000
    else:
        M=pl[0]
    total = count_full_primes(M, digits)
    smaller_pl = [p for p in pl if set(str(p)).intersection(set(digits)) == set(str(p))]

    for i in range(len(smaller_pl)):
        p = smaller_pl[i]
        new_digits = ''.join([d for d in digits if d not in str(p)])
        if new_digits:
            total += get_n_partitions(smaller_pl[i+1:],new_digits)

    return total

print(get_n_partitions(small_primelist,'123456789'))



