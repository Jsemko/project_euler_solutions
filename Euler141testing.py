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
primelist = primes_under(int(1000000**.5)+1)

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

factor_dict=dict()
square_part=dict()

from collections import Counter

for i in range(2,1000000):
    if (i + 1) % 100000 == 0: print('done ' + str(i))
    factor_dict[i] = prime_factor(i)
    current_primes = set(factor_dict[i])
    den = 1
    c = Counter(factor_dict[i])
    for p in current_primes:
        den*=(p**(c[p]//2))
    square_part[i]=den

square_part[1] = 1

print(square_part[6])
print(square_part[9])

def is_square(n):
    return round(n**.5)**2 == n

all_found = set()

# first one q<r<d
"""
first_count = 0
for q in range(2,998001):
    if (q + 1) % 100000 == 0: print('done ' + str(q))
    sp = square_part[q]
    den = sp
    num = den +1
    r,d =  (num*q) // den , (num**2 * q) // (den**2)
    n = q*d +r
    while n < 1e12:
        if is_square(n):
            first_count+=1
            all_found.add(n)
        num +=1
        r, d = (num * q) // den, (num ** 2 * q) // (den ** 2)
        n = q * d + r

print('first count = {c}'.format(c = first_count))

"""
# second r<q<d
second_count = 0
for r in range(1,998001):
    if (r + 1) % 100000 == 0: print('done ' + str(r))
    sp = square_part[r]
    den = sp
    num = den +1
    q,d =  (num*r) // den , (num**2 * r) // (den**2)
    n = q*d +r
    while n < 1e12:
        if is_square(n):
            second_count+=1
            all_found.add(n)
        num +=1
        q, d = (num * r) // den, (num ** 2 * r) // (den ** 2)
        n = q * d + r


print(second_count)
print(sum(all_found))

print(list(all_found)[:20])

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


