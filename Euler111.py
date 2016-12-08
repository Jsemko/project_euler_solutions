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

L = len(primelist)

def is_prime(n):
    start = 0
    M = int(n**.5+1)
    p = primelist[start]
    while  p < M:
        if n % p == 0:return False
        start +=1
        if start >= len(primelist):break
        p = primelist[start]
    return True

int_length = 10

import itertools

def has_max(digit, length):
    digit = str(digit)
    indicies = list(range(int_length))
    others = list('0123456789')
    others.remove(digit)
    for subset in itertools.combinations(indicies,length):
        for replace in itertools.product(others,repeat=length):
            full_str = digit * int_length
            for i in range(length):
                full_str = full_str[:subset[i]] + replace[i] + full_str[subset[i]+1:]
            if full_str[0] == '0': continue
            if is_prime(int(full_str)):
                print(int(full_str))
                return True
    return False

total_sum = 0

def sum_all(digit,length):
    this_sum = 0
    digit = str(digit)
    indicies = list(range(int_length))
    others = list('0123456789')
    others.remove(digit)
    for subset in itertools.combinations(indicies, length):
        for replace in itertools.product(others, repeat=length):
            full_str = digit * int_length
            for i in range(length):
                full_str = full_str[:subset[i]] + replace[i] + full_str[subset[i] + 1:]
            if full_str[0] == '0': continue
            if is_prime(int(full_str)):
                this_sum += int(full_str)
    return this_sum

dict_to_try = {0:2,1:1,2:2,3:1,4:1,5:1,6:1,7:1,8:2,9:1}

for k,v in dict_to_try.items():
    total_sum += sum_all(k,v)
print(total_sum)

